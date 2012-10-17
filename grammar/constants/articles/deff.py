from pyparsing import *

from ...functions.deff import oneOfNamed

from decl import *

TARGET << CaselessLiteral("target")
THIS << CaselessKeyword("this")
THAT << CaselessKeyword("that")
AN << oneOfNamed ("a an")
THE << CaselessLiteral("the")
OTHER << CaselessLiteral("other")
ANOTHER << CaselessLiteral("another")
ALL << CaselessLiteral("all")
EACH << CaselessLiteral("each")
