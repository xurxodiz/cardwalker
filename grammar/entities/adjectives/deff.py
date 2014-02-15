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

# 'and' captures both 'legendary creature' (juxtaposed) and 'black and red' (joined)

# 'or' will capture explicit disjunctions 'black or red'
# but since it will come after the ^, not juxtapositions (taken by 'and')

# so the 'one or more' allows 'legendary black or red'
# to be correctly interpreted as (A and (B or C))
# it's non-intuitive, but it works

# at the same time, it forces us to use ^ instead of |
# or "target artifact, enchantment or land"
# becomes ((A and B) or C)

andadjectives << delimitedListAnd(adjective)

oradjectives << delimitedListOr(adjective)

adjectives << OneOrMore(andadjectives ^ oradjectives)