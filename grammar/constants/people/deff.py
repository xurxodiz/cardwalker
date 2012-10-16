from pyparsing import *

from ..punctuation.deff import APOS
from ...functions.deff import *
from decl import *

CONTROLLER << oneOfNamed("controller controllers")
OWNER << oneOfNamed("owner owners")
YOU << CaselessLiteral("you")
PLAYER << oneOfNamed("player players")
OPPONENT << oneOfNamed("opponent opponents")
YOUR << CaselessLiteral("your")
HIS << CaselessLiteral("his or her")
THEIR << CaselessLiteral("their")
POSS << (CaselessLiteral("'s") | APOS)