from pyparsing import *

from ...functions.deff import oneOfNamed, loadLinesFromFile

from decl import *

SPELL << oneOfNamed("spell spells")
PERMANENT << oneOfNamed("permanent permanents")
CARD << oneOfNamed("card cards")

THISCARD << Literal("~")
NAMES << loadLinesFromFile("oracle/ref/names.txt")

COUNTER << CaselessLiteral("counter") # +1/+1 etc