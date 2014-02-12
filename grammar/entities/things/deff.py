from pyparsing import *

from ..adjectives.deff import adjectives
from ..articles.deff import det
from ..zones.deff import where
from ...types.deff import subtype, type_, thiscard
from ...constants.concepts.deff import SPELL, PERMANENT, CARD
from ...functions.deff import delimitedListAnd, delimitedListOr

from decl import *

concept << (SPELL|PERMANENT|CARD)

noun << (subtype | type_ | concept)

andnoun << delimitedListAnd(noun)
ornoun << delimitedListOr(noun)

basething << OneOrMore(andnoun ^ ornoun)

thing << Optional(det) + Optional(adjectives) + basething
orthings << delimitedListOr(thing)
andthings << delimitedListAnd(thing)

things << OneOrMore(
	(andthings ^ orthings) + Optional(where)
)