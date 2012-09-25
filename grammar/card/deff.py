from pyparsing import *

from ..basic.constants.deff import EOL
from ..types.deff import cardtypeline
from ..mana.deff import cardcost
from ..ptl.deff import cardptl
from ..rules.deff import cardrules
from ..exp.deff import cardexpansions

from decl import *

ParserElement.setDefaultWhitespaceChars(" \t")

"""
cardname
"""

card << (
	Optional(cardcost)
	+ cardtypeline
	+ cardptl
	+ cardrules
	+ cardexpansions
)