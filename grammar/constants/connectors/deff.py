from pyparsing import *

from decl import *

AND << CaselessLiteral("and")
OR << CaselessLiteral("or")

IF << CaselessLiteral("if")

WHEN << CaselessLiteral("when")
WHENEVER << CaselessLiteral ("whenever")
WHERE << CaselessLiteral("where")
