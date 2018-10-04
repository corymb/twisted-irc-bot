# IRC Network
IRC_HOST = 'irc.freenode.net'
IRC_PORT = 6667

# Bot:
NICK = 'irc_bot'
CHANNEL = '##BotTesting'

# Log file location:
LOG_FILE_LOCATION = '{}.log'.format(NICK)

# How many lines of scrollback to retain:
SCROLLBACK_SIZE = 1000

# Character to call bot's commands:
COMMAND_CHARACTER = '!'

# Message sent on join (set to None if not desired):
JOIN_MESSAGE = 'Hi! I am {}'.format(NICK)

# Relative path to file for storing quotes:
QUOTE_FILE_LOCATION = 'quotes.txt'

# Format for interpolation:
QUOTE_FORMAT = '{} - <{}>: {}\n'

# Message to show if the search string isn't present in scrollback:
QUOTE_NOT_FOUND_MESSAGE = '[Quote not found]'

# Message to show if quote save failed:
QUOTE_SAVE_FAILED = 'Could not save'

# Text to append to aesthetic command:
AESTHETIC_STRING = '  a e s t h e t i c'
