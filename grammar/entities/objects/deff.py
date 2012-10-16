from pyparsing import *

from ..adjectives.deff import adjectives
from ..people.deff import peopleposs
from ..articles.deff import det
from ..zones.deff import where
from ...types.deff import subtype, type_, cardname
from ...constants.concepts.deff import IT, THEY, concept
from ...functions.deff import delimitedListAnd, delimitedListOr

from decl import *

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
	| cardname
	| it
	| they
	) + Optional(where)
)