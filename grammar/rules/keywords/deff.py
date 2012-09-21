from pyparsing import *

from ...basic.constants.deff import *
from ...basic.functions.deff import *
from ...ptl.deff import *
from ...mana.deff import *
from ...types.deff import *

from decl import *

PROTECTION << CaselessLiteral("Protection")
WALK << CaselessLiteral("Walk")

INDESTRUCTIBLE << CaselessLiteral("indestructible")
UNBLOCKABLE << CaselessLiteral("unblockable")

EQUIP << oneOfNamed ("equip equipped")
FORTIFY << oneOfNamed ("fortify fortified")
HAUNT << oneOfNamed ("haunt haunted")
ENCHANT << oneOfNamed ("enchant enchanted")
"""
landwalk << objects + WALK # legendary/nonbasic/forest/etc land
"""
basic_keyword << load_from_file("oracle/ref/basic_keywords.txt")

number_keyword << load_from_file("oracle/ref/number_keywords.txt") + NUMBER
CYCLING << CaselessLiteral("Cycling")
cycling << Optional(basic_land_type|subtype) + CYCLING

costed_keyword << (load_from_file("oracle/ref/costed_keywords.txt")
#				| EQUIP
#				| FORTIFY
				| cycling
) + manapayment

protection << Suppress(PROTECTION) + delimitedListAnd(Suppress(FROM) + color)
"""
ability_keyword << load_from_file("oracle/ref/ability_keywords.txt")

enchant << ENCHANT + objects
"""
keywords << delimitedListAnd( \
		protection
		| basic_keyword
		| number_keyword
		| costed_keyword
)
"""
		#|number_keyword + (DASH + cardrules))
		#| costed_keyword + (DASH + oneshot)) 
		| ability_keyword + DASH + cardrules
		| enchant
		| landwalk
		| enchant
)"""