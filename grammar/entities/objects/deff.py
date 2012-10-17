from pyparsing import *

from ..adjectives.deff import adjectives
from ..articles.deff import det
from ..zones.deff import where
from ...types.deff import subtype, type_, name
from ...constants.concepts.deff import IT, THEY, SPELL, PERMANENT, CARD, ABILITY
from ...functions.deff import delimitedListAnd, delimitedListOr

from decl import *

concept << (SPELL|PERMANENT|CARD)

noun << (subtype | type_ | concept)

andnoun << delimitedListAnd(noun)
ornoun << delimitedListOr(noun)

baseobject_ << OneOrMore(andnoun ^ ornoun)

object_ << Optional(det) + Optional(adjectives) + baseobject_
orobjects << delimitedListOr(object_)
andobjects << delimitedListAnd(object_)

it << IT
they << THEY

objects << OneOrMore(
	(andobjects ^ orobjects
	| name
	| it
	| they
	) + Optional(where)
)