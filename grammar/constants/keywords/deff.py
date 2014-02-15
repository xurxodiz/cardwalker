from pyparsing import *

from ...functions.deff import loadFromFile, loadLinesFromFile
from decl import *

PROTECTION << CaselessLiteral("Protection")
WALK << CaselessLiteral("Walk")

BASICKEYWORD << loadLinesFromFile("oracle/ref/basic_keywords.txt")

NUMBERKEYWORD << loadLinesFromFile("oracle/ref/number_keywords.txt")

COSTEDKEYWORD << loadLinesFromFile("oracle/ref/costed_keywords.txt")

CYCLING << CaselessLiteral("cycling")