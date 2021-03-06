from pyparsing import *

from ...functions.deff import oneOfNamed

from decl import *

TOP << CaselessLiteral("top")
BOTTOM << CaselessLiteral("bottom")

HAND << oneOfNamed("hand hands")
GRAVEYARD << oneOfNamed("graveyard graveyards")
LIBRARY << oneOfNamed("library libraries")
# exile is defined in the verb module
BATTLEFIELD << CaselessLiteral("battlefield")