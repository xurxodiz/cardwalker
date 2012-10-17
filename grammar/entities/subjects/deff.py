from pyparsing import *

from ..people.deff import people
from ..things.deff import things
from ...constants.verbs.deff import MAY, HAVE
from ...functions.deff import delimitedListOr, delimitedListAnd

from decl import *

orobjects << delimitedListOr(people|things) 
andobjects << delimitedListAnd(people|things)
objects << (andobjects ^ orobjects)

mayhave << people + MAY + HAVE + objects
may << people + MAY

subjects << (mayhave|may|objects)