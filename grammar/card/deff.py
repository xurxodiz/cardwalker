from pyparsing import *

ParserElement.setDefaultWhitespaceChars("\t ")

from ..constants.punctuation.deff import EOL
from ..types.deff import cardtypeline, cardname
from ..mana.deff import cardcost
from ..ptl.deff import cardptl
from ..rules.deff import cardrules
from ..expansions.deff import cardexpansions

from decl import *

card << (cardname
	+ Optional(cardcost)
	+ cardtypeline
	+ Optional(cardptl)
	+ Optional(cardrules)
	+ cardexpansions
)