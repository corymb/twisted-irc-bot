from collections import deque
from datetime import datetime
from random import random

from twisted.python import log

import config as c


class Bot:
    def __init__(self):
        self.messages = deque(maxlen=c.SCROLLBACK_SIZE)

    # Commands:
    def command_save(self, query):
        for m in self.messages:
            if query.strip() in m:
                self.write_message_to_file(m)
                return 'Saved: "{}"'.format(m.text)
        else:
            log.msg('Quote not found')
            return c.QUOTE_NOT_FOUND_MESSAGE

    def command_aesthetic(self, text):
        # Returns based on text case
        formatted_text = ' '.join(c for c in text)
        log.msg('{} aesthetic'.format(text.strip()))
        if text.islower():
            return formatted_text.lstrip() + c.AESTHETIC_STRING
        return formatted_text.lstrip() + c.AESTHETIC_STRING.upper()

    def command_probability(self, text):
        return c.PROBABILITY_STRING.format(text.strip(), random())

    # Utils:
    def write_message_to_file(self, message, target=c.QUOTE_FILE_LOCATION):
        with open(target, 'a') as f:
            quote = c.QUOTE_FORMAT.format(
                    message.time, message.sender, message.text)
            f.write(quote)
            log.msg('Quote added: {}'.format(quote))


class Message:
    def __init__(self, sender, text):
        self.sender = self._get_message_nick(sender)
        self.text = text.strip()
        self.time = datetime.now()
        log.msg('Message logged: <{}>: {}'.format(self.sender, self.text))

    def _get_message_nick(self, user):
        return user.split('!')[0]

    def __contains__(self, substring):
        log.msg('Quote search query: {}'.format(substring))
        return substring in self.text

    def __repr__(self):
        return 'Message: '.format(self.text)
