from pyparsing import *

from ..constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM
from ..constants.people.deff import *
from decl import *

change << Optional(PLUS|MINUS) + amount
amount << ((NUM + change) | NUM | (XVAR + change) | XVAR | FULLNUM)

quantity << ( \
		amount
		| UPTO + amount
		| AN
		| ANOTHER
		| ALL
)

det << ( \
	TARGET
	| quantity + TARGET
	| quantity
	| peopleposs
	| (THIS|THAT)
	| OTHER
	| EACH
	| ITS
	| THE
)

people << Optional(det) + (YOU | PLAYER | OPPONENT | CONTROLLER | OWNER)

peopleposs << (YOUR
		| THEIR
		| HIS
		| people + POSS
)

zone << ( \
		peopleposs + (GRAVEYARD|HAND|LIBRARY)
		| det + delimitedListAndOr(GRAVEYARD|HAND|LIBRARY)
		| THE + BATTLEFIELD 
		| THE + TOP + OF + peopleposs + LIBRARY
)

adj << (delimitedListAndOr( \
	color
	| nontype
	| supertype
	| (TOP|BOTTOM) + number
	# coming next: participles
	| TAP
	| UNTAP
	| ENCHANT
	| EQUIP
	| EXILE
	| SACRIFICE
	| HAUNT
))

where << (people + CONTROL
		| IN + zone
		| OF + zone
		| FROM + zone
)

concept << (SPELL | PERMANENT | CARD | ABILITY)

obj << (Optional(adj)
	+ delimitedListAndOr(subtype | type_ | concept)
	+ Optional(where)
)

objects << (\
	delimitedListAndOr(det + obj | obj)
	| IT
	| peopleposs + LIFE + TOTAL
	| det + TOP + fullnumber + CARD + OF + zone
	| cardname
)

resources << ( \
	peopleposs + LIFE + TOTAL
	| peopleposs + HAND + SIZE
)

mayer << people + Optional(MAY + Optional(people|objects))
subject << (resources|mayer|people|objects)