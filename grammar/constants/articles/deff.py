from pyparsing import *

from ...functions.deff import oneOfNamed
from ..punctuation.deff import APOS

from decl import *

TARGET << CaselessLiteral("target")
THIS << CaselessKeyword("this")
THAT << CaselessKeyword("that")
AN << oneOfNamed ("a an")
THE << CaselessLiteral("the")
OTHER << CaselessLiteral("other")
ANOTHER << CaselessLiteral("another")
HIS << CaselessLiteral("his or her")
ALL << CaselessLiteral("all")
EACH << CaselessLiteral("each")
ITS << oneOfNamed("its their")
YOUR << CaselessLiteral("your")
THEIR << CaselessLiteral("their")
POSS << (CaselessLiteral("'s") | APOS)
