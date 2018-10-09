import os

# IRC Network
IRC_HOST = os.getenv('IRC_BOT_HOST', 'irc.freenode.net')
IRC_PORT = os.getenv('IRC_BOT_PORT', 6667)

# Bot:
NICK = os.getenv('IRC_BOT_NICK', 'irc_bot')
CHANNEL = os.getenv('IRC_BOT_CHANNEL', '##BotTesting')

# Log file location:
LOG_FILE_LOCATION = os.getenv('IRC_BOT_LOG_FILE_LOCATION', '{}.log'.format(NICK))

# How many lines of scrollback to retain:
SCROLLBACK_SIZE = os.getenv('IRC_BOT_SCROLLBACK_SIZE', 1000)

# Character to invoke bot's commands:
COMMAND_CHARACTER = os.getenv('IRC_BOT_COMMAND_CHARACTER', '!')

# Message sent on join (set to None if not desired):
JOIN_MESSAGE = os.getenv('IRC_BOT_JOIN_MESSAGE', 'Hi! I am {}'.format(NICK))

# Relative path to file for storing quotes:
QUOTE_FILE_LOCATION = os.getenv('IRC_BOT_QUOTE_FILE_LOCATION', 'quotes.txt')

# Format for interpolation:
QUOTE_FORMAT = os.getenv('IRC_BOT_QUOTE_FORMAT', '{} - <{}>: {}\n')

# Message to show if the search string isn't present in scrollback:
QUOTE_NOT_FOUND_MESSAGE = os.getenv('IRC_BOT_QUOTE_NOT_FOUND_MESSAGE', '[Quote not found]')

# Message to show if quote save failed:
QUOTE_SAVE_FAILED = os.getenv('IRC_BOT_QUOTE_SAVE_FAILED', 'Could not save quote')

# Text to append to aesthetic command:
AESTHETIC_STRING = os.getenv('IRC_BOT_AESTHETIC_STRING', '  a e s t h e t i c')
