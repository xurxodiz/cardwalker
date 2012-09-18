from pyparsing import *

from ..basic.constants.deff import card
#from types import cardtypeline
#from pt import cardpt
from ..expansions import cardexpansions

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

cardtypeline = (PLAYER|OPPONENT)

card << (
	cardtypeline #+ EOL
	#+ cardpt + EOL
	#+ cardexpansions + EOL
)
