from pyparsing import *

from decl import *

NEXT << CaselessLiteral("next")
EQUAL << CaselessLiteral("equal")

NON << CaselessLiteral("non")
ATRANDOM << CaselessLiteral("at random")
ALONE << CaselessLiteral("alone")