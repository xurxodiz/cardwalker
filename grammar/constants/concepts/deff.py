from pyparsing import *

from decl import *

IT << CaselessLiteral("it")
SPELL << oneOfNamed("spell spells", caseless=True)
PERMANENT << oneOfNamed("permanent permanents", caseless=True)
CARD << oneOfNamed("card cards", caseless=True)
ABILITY << oneOfNamed("ability abilities", caseless=True)
COUNTER << CaselessLiteral("counter")