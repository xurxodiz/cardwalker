from pyparsing import *

from ...constants.math.deff import NUM, FULLNUM
from ...constants.zones.deff import TOP, BOTTOM
from ...constants.verbs.deff import *
from ...mana.deff import color
from ...types.deff import nontype, supertype
from ...functions.deff import delimitedListAnd, delimitedListOr

from decl import *

topnum << (TOP|BOTTOM) + (NUM|FULLNUM)

attacking << ATTACK
blocking << BLOCK
tapped << TAP
untapped << UNTAP
enchanted << ENCHANT
equipped << EQUIP
exiled << EXILE
sacrificed << SACRIFICE
haunted << HAUNT

adjective << (
	color
	| nontype
	| supertype
	| topnum
	| attacking
	| blocking
	| tapped
	| untapped
	| enchanted
	| equipped
	| exiled
	| sacrificed
	| haunted
)

andadjectives << delimitedListAnd(adjective)
oradjectives << delimitedListOr(adjective)

adjectives << OneOrMore(andadjectives ^ oradjectives)