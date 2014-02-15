from pyparsing import *

from ...constants.concepts.deff import SPELL, PERMANENT, CARD, THISCARD
from ...constants.modifiers.deff import NAMED
from ...functions.deff import delimitedListAnd, delimitedListOr, loadLinesFromFile
from ...types.deff import subtype, type_
from ..adjectives.deff import adjectives
from ..articles.deff import det
from ..zones.deff import where

from decl import *

name << loadLinesFromFile("oracle/ref/names.txt")
thiscard << THISCARD

named << NAMED + (thiscard | name)

concept << (SPELL|PERMANENT|CARD)

noun << (subtype | type_ | concept) #+ Optional(named)

andnoun << delimitedListAnd(noun)
ornoun << delimitedListOr(noun)

basething << OneOrMore(andnoun ^ ornoun)

thing << Optional(det) + Optional(adjectives) + basething
orthings << delimitedListOr(thing)
andthings << delimitedListAnd(thing)

things << (
  thiscard
  | OneOrMore((andthings ^ orthings) + Optional(where))
)
