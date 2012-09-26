from pyparsing import *

from ...functions.deff import *
from decl import *

CONTROLLER << oneOfNamed("controller controllers")
OWNER << oneOfNamed("owner owners")
YOU << CaselessLiteral("you")
PLAYER << oneOfNamed("player players")
OPPONENT << oneOfNamed("opponent opponents")