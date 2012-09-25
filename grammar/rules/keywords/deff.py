from pyparsing import *

from ...basic.constants.deff import FROM, NUM
from ...basic.functions.deff import oneOfNamed, loadFromFile, delimitedListAnd
from ...mana.deff import color, manapayment
from ...types.deff import land_type, subtype

from decl import *

PROTECTION << CaselessLiteral("Protection")
WALK << CaselessLiteral("Walk")

INDESTRUCTIBLE << CaselessLiteral("indestructible")
UNBLOCKABLE << CaselessLiteral("unblockable")

EQUIP << oneOfNamed ("equip equipped")
FORTIFY << oneOfNamed ("fortify fortified")
HAUNT << oneOfNamed ("haunt haunted")
ENCHANT << oneOfNamed ("enchant enchanted")

landwalk << land_type + WALK
# landwalk2 << objects + WALK # legendary/nonbasic/forest/etc land

basic_keyword << loadFromFile("oracle/ref/basic_keywords.txt")

number_keyword << loadFromFile("oracle/ref/number_keywords.txt") + NUM

costed_keyword << loadFromFile("oracle/ref/costed_keywords.txt") + manapayment

# cycling goes apart because we need to extract the type
CYCLING << Suppress(CaselessLiteral("cycling"))
cycling << Optional(subtype) + CYCLING + manapayment

protection << Suppress(PROTECTION) + delimitedListAnd(Suppress(FROM) + color)

"""
ability_keyword << loadFromFile("oracle/ref/ability_keywords.txt")

enchant << ENCHANT + objects
"""

keywords << delimitedListAnd( \
		protection
		| basic_keyword
		| number_keyword
		| costed_keyword
		| cycling
		| landwalk
)

"""
		|number_keyword + (DASH + cardrules)
		| costed_keyword + (DASH + oneshot)) 
		| ability_keyword + DASH + cardrules
		| enchant
		| equip
		| haunt
		| fortify
)"""