from pyparsing import *

from ..basic.constants.deff import *
from ..types.deff import cardtypeline
from ..mana.deff import cardcost
from ..ptl.deff import cardptl
from ..rules.keywords.deff import protection, keywords
from ..exp.deff import cardexpansions

from decl import *

ParserElement.setDefaultWhitespaceChars(" \t")

"""
card = (cardname + EOL
	+ Optional(cardcost + EOL)
	+ cardtypeline + EOL
	+ Optional(cardpt + EOL)
	+ Optional(cardrules + EOL)
	+ cardexpansions + EOL
)
"""


card << (
	Optional(cardcost)
	+ cardtypeline
	+ cardptl
	+ protection + EOL
	+ cardexpansions
)
