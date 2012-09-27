from pyparsing import *

from ...functions.deff import oneOfNamed

from decl import *

IT << CaselessLiteral("it")
SPELL << oneOfNamed("spell spells")
PERMANENT << oneOfNamed("permanent permanents")
CARD << oneOfNamed("card cards")
ABILITY << oneOfNamed("ability abilities")
COUNTER << CaselessLiteral("counter")

concept << (SPELL|PERMANENT|CARD|ABILITY)