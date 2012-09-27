from pyparsing import *

from ...functions.deff import loadFromFile
from decl import *

PROTECTION << CaselessLiteral("Protection")
WALK << CaselessLiteral("Walk")

INDESTRUCTIBLE << CaselessLiteral("indestructible")
UNBLOCKABLE << CaselessLiteral("unblockable")

BASICKEYWORD << loadFromFile("oracle/ref/basic_keywords.txt")

NUMBERKEYWORD << loadFromFile("oracle/ref/number_keywords.txt")

COSTEDKEYWORD << loadFromFile("oracle/ref/costed_keywords.txt")

CYCLING << CaselessLiteral("cycling")