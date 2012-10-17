from pyparsing import *

from ..punctuation.deff import APOS
from ...functions.deff import *
from decl import *

CONTROLLER << oneOfNamed("controller controllers")
OWNER << oneOfNamed("owner owners")

PLAYER << oneOfNamed("player players")
OPPONENT << oneOfNamed("opponent opponents")

YOU << CaselessLiteral("you")
YOUR << CaselessLiteral("your")

HE << CaselessLiteral("he or she")
HIS << CaselessLiteral("his or her")

THEY << CaselessLiteral("they")
THEIR << CaselessLiteral("their")

IT << CaselessLiteral("it")
ITS << CaselessLiteral("its")

POSS << (CaselessLiteral("'s") | APOS)