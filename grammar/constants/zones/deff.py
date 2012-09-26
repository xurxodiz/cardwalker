from pyparsing import *

from decl import *

TOP << CaselessLiteral("top")
BOTTOM << CaselessLiteral("bottom")

HAND << oneOfNamed("hand hands", caseless=True)
GRAVEYARD << oneOfNamed("graveyard graveyards", caseless=True)
LIBRARY << oneOfNamed("library libraries", caseless=True)
# exile is defined as verb
BATTLEFIELD << CaselessLiteral("battlefield")