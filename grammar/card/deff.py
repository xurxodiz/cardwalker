from pyparsing import *

ParserElement.setDefaultWhitespaceChars("\t ")

from ..constants.punctuation.deff import DASH, COMMA, EOL
from ..types.deff import supertype, type_, subtype, name
from ..mana.deff import singlecost
from ..ptl.deff import ptstart, loyaltystart
from ..rules.deff import rulelist
from ..expansions.deff import expansion

from decl import *

cardname << name + EOL

cardcost << (OneOrMore(singlecost) + EOL)

cardsupertypes << OneOrMore(supertype)
cardtypes << OneOrMore(type_)
cardsubtypes << OneOrMore(subtype)

cardtypeline << (
	Optional(cardsupertypes)
	+ cardtypes
	+ Optional(Suppress(DASH) + cardsubtypes)
	+ EOL
)

cardptl << (ptstart|loyaltystart) + EOL

cardrules << OneOrMore(rulelist + EOL)

cardexpansions << (delimitedList(expansion, COMMA) + EOL)

card << (cardname
	+ Optional(cardcost)
	+ cardtypeline
	+ Optional(cardptl)
	+ Optional(cardrules)
	+ cardexpansions
)