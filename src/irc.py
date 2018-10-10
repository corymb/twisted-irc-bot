from twisted.internet import defer, protocol
from twisted.python import log
from twisted.words.protocols import irc

import config as c
from bot import Bot, Message


class IRCProtocol(irc.IRCClient):
    nickname = c.NICK

    def signedOn(self):
        self.join(self.factory.channel)
        log.msg('Joined channel: {}'.format(self.factory.channel))
        if c.JOIN_MESSAGE:
            self.msg(user=self.factory.channel, message=c.JOIN_MESSAGE)
            log.msg('Sent JOIN message: {}'.format(c.JOIN_MESSAGE))

    def privmsg(self, user, channel, message):
        return self._message_handler(user, channel, message)

    def kickedFrom(self, channel, kicker, message):
        log.msg('Got kicked by {}'.format(kicker))
        self.signedOn()


    def _message_handler(self, sender, channel, message):
        saved_message = Message(sender=sender, text=message)
        if not saved_message.text.startswith(c.COMMAND_CHARACTER):
            self.factory.bot.messages.appendleft(saved_message)
            return

        # Command dispatch:
        command, *message_text = saved_message.text.lstrip('!').partition(' ')
        log.msg('Command sent: {}'.format(command))
        func = getattr(self.factory.bot, 'command_' + command, None)
        if func is None:
            return

        # Wrap in deferred for non-blocking:
        d = defer.maybeDeferred(func, ' '.join(message_text))
        d.addCallbacks(
            self._messageChannelSuccess,
            self._messageChannelFailure
        )

    def _messageChannelSuccess(self, message):
        self.msg(user=self.factory.channel, message=message)

    def _messageChannelFailure(self, failure):
        log.err(failure.getErrorMessage())
        self.msg(user=self.factory.channel, message=c.QUOTE_SAVE_FAILED)


class IRCBotFactory(protocol.ClientFactory):
    protocol = IRCProtocol

    def __init__(self):
        self.channel = c.CHANNEL
        self.bot = Bot()
