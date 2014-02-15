from pyparsing import *

from decl import *

NEXT << CaselessLiteral("next")
EQUAL << CaselessLiteral("equal")

NON << CaselessLiteral("non")
ATRANDOM << CaselessLiteral("at random")

ABLE << CaselessLiteral("able")
ALONE << CaselessLiteral("alone")

COMBAT << CaselessLiteral("combat")

NAMED << CaselessLiteral("named")