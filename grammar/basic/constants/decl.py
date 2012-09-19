from pyparsing import *

import act

EOL = Forward()

APOS = Forward()

PLUS = Forward()
MINUS = Forward()

QUOTE = Forward()
COMMA = Forward()
POINT = Forward()

LPAREN = Forward()
RPAREN = Forward()
LBRACE = Forward()
RBRACE = Forward()
LBRACKET = Forward()
RBRACKET = Forward()

XVAR = Forward().setParseAction(lambda x: "X")
SLASH = Forward()
DASH = Forward()
COLON = Forward()

DIGIT = Forward()
NUM = Forward().setParseAction(lambda x: int(x[0]))
FULLNUM = Forward().setParseAction(act.fullnum)

UPPERCASE = Forward()

AND = Forward()
OR = Forward()

NON = Forward()

THIS = Forward()
THAT = Forward()
IT = Forward()

AN = Forward()
THE = Forward()
OTHER = Forward()
ANOTHER = Forward()
HIS = Forward()
ALL = Forward()
EACH = Forward()
ITS = Forward()
YOUR = Forward()
THEIR = Forward()
POSS = Forward()

WHEN = Forward()
WHERE = Forward()
TARGET = Forward()
MAY = Forward()
TO = Forward()
UPTO = Forward()
OF = Forward()
IN = Forward()
ON = Forward()
ONTO = Forward()
INTO = Forward()
WITH = Forward()
FROM = Forward()
BY = Forward()
AT = Forward()
FOR = Forward()
UNTIL = Forward()
UNDER = Forward()
NEXT = Forward()
WITH = Forward()
EQUAL = Forward()

BE = Forward()
HAVE = Forward()
GET = Forward()
CANT = Forward()
MUST = Forward()

DESTROY = Forward()
EXILE = Forward()
GAIN = Forward()
LOSE = Forward()
TAP = Forward()
UNTAP = Forward()
DISCARD = Forward()
SACRIFICE = Forward()
DRAW = Forward()
DEAL = Forward()
PAY = Forward()
PUT = Forward()
ATTACK = Forward()
BLOCK = Forward()
BECOME = Forward()
REDUCE = Forward()
RETURN = Forward()
ENTER = Forward()
LEAVE = Forward()
DIE = Forward()
PREVENT = Forward()
ADD = Forward()
REGENERATE = Forward()
CONTROL = Forward()

SPELL = Forward()
PERMANENT = Forward()
CARD = Forward()
ABILITY = Forward()
COUNTER = Forward()
COUNTERSPELL = Forward()

CONTROLLER = Forward()
OWNER = Forward()
YOU = Forward()
PLAYER = Forward()
OPPONENT = Forward()

HAND = Forward()
GRAVEYARD = Forward()
LIBRARY = Forward()
EXILE = Forward()
BATTLEFIELD = Forward()

ATRANDOM = Forward()
ALONE = Forward()

TOTAL = Forward()
SIZE = Forward()
NUMBER = Forward()

BEGINNING = Forward()
END = Forward()
TOP = Forward()
BOTTOM = Forward()

TURN = Forward()
UPKEEP = Forward()
DRAWSTEP = Forward()
PRECOMBAT = Forward()
COMBAT = Forward()
POSCOMBAT = Forward()

DAMAGE = Forward()
LIFE = Forward()
MANA = Forward()
POOL = Forward()
SOURCE = Forward()
