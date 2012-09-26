from pyparsing import *

from ...functions.deff import *
from decl import *

COLORNAME << oneOf("white blue black red green", caseless=True)
COLORFEATURE << oneOf ("colorless colored multicolored monocolored", caseless=True)
MANASYMBOL << oneOf("W U B R G", caseless=True)
TAPSYMBOL << CaselessLiteral("T")
UNTAPSYMBOL << CaselessLiteral("Q")
SNOWSYMBOL << CaselessLiteral("S")
PHYSYMBOL << CaselessLiteral("P")

FREQUENCY << oneOf("M R U C L S")

DAMAGE << CaselessLiteral("damage")
LIFE << CaselessLiteral("life")
MANA << CaselessLiteral("mana")
POOL << CaselessLiteral("pool")
SOURCE << oneOfNamed("source sources")

TOTAL << CaselessLiteral("total")
SIZE << CaselessLiteral("size")
NUMBER << CaselessLiteral("number")