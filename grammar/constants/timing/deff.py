from pyparsing import *

from decl import *

BEGINNING << CaselessLiteral("beginning")
END << CaselessLiteral("end")

TURN << CaselessLiteral("turn")
UPKEEP << CaselessLiteral("upkeep")
DRAWSTEP << CaselessLiteral("draw step")
PRECOMBAT << CaselessLiteral("first main phase")
COMBAT << CaselessLiteral("combat phase")
POSCOMBAT << CaselessLiteral("second main phase")