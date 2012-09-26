from pyparsing import *

EOL = Forward()

QUOTE = Forward()
COMMA = Forward()
POINT = Forward()

LPAREN = Forward()
RPAREN = Forward()
LBRACE = Forward()
RBRACE = Forward()
LBRACKET = Forward()
RBRACKET = Forward()

SLASH = Forward()
DASH = Forward()
COLON = Forward()

APOS = Forward()