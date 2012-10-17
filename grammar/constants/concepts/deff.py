from pyparsing import *

from ...functions.deff import oneOfNamed

from decl import *

SPELL << oneOfNamed("spell spells")
PERMANENT << oneOfNamed("permanent permanents")
CARD << oneOfNamed("card cards")

COUNTER << CaselessLiteral("counter") # +1/+1 etc