from pyparsing import *

from ...constants.articles.deff import *
from ...constants.connectors.deff import WHERE
from ...constants.concepts.deff import COUNTER
from ...constants.math.deff import XVAR
from ...constants.modifiers.deff import NEXT, NON, EQUAL, ATRANDOM
from ...constants.prepositions.deff import *
from ...constants.punctuation.deff import POINT
from ...constants.resources.deff import DAMAGE, LIFE, NUMBER, MANA, POOL
from ...constants.timing.deff import COMBAT, TURN
from ...constants.verbs.deff import *
from ...entities.deff import quantity, subject, objects, zone, peopleposs
from ...mana.deff import manapayment
from ...ptl.deff import ptstart, ptmod

from ...functions.deff import *
from ..keywords.deff import keywords
from decl import *

nextquantity << THE + NEXT + quantity

damage << (quantity|nextquantity) + DAMAGE
combatdamage << (quantity|nextquantity) + COMBAT + DAMAGE
noncombatdamage << (quantity|nextquantity) + NON + COMBAT + DAMAGE

thedamage << (damage|noncombatdamage|combatdamage)

thisturn << THIS + TURN

where << (Suppress(WHERE + XVAR + BE + Optional(THE+NUMBER+OF)) + objects)
equal << (Suppress(EQUAL + TO + THE + NUMBER + OF) + objects)
for_ << (FOR + objects)

undercontrol << (UNDER + peopleposs + CONTROL)

destroy << DESTROY + objects
cantregenerate << CANT + BE + REGENERATE
exile << EXILE + objects + Optional(FROM + delimitedListAnd(zone))
gainlife << GAIN + quantity + LIFE
tap << TAP + objects
untap << UNTAP + objects
draw << DRAW + objects
discard << DISCARD + objects + Optional(ATRANDOM)
loselife << LOSE + quantity + LIFE
dealquantitydamage << DEAL + quantity + DAMAGE + TO + objects
dealdamage << DEAL + DAMAGE + TO + objects
sacrifice << SACRIFICE + objects
regenerate << REGENERATE + objects
putcounter << PUT + quantity + ptmod + COUNTER + ON + objects 

tokens << ptstart + objects + Optional(Suppress(WITH) + delimitedListAnd(keywords))

puttoken << (Suppress(PUT) + quantity + tokens
		+ Suppress(ONTO) + zone + Optional(undercontrol)
)

return_ << (Suppress(RETURN) + objects
	+ Optional(Suppress(FROM) + delimitedListAnd(zone))
	+ Suppress(TO) + zone
	+ Optional(undercontrol)
)

become << BECOME + quantity # for life totals
bereduced << BE + REDUCE + BY + quantity
paylife << PAY + quantity + LIFE

prevention << (Suppress(PREVENT) + thedamage + Suppress(THAT + WOULD + BE + DEAL)
		+ Optional(thisturn)
		+ Suppress(TO) + objects
		+ Optional(thisturn)
)

addmana << ADD + manapayment + TO + peopleposs + MANA + POOL

counterspell << COUNTERSPELL + objects

quantifier << (for_ | Suppress(COMMA) + (where|equal))

effect << (
		destroy
		| cantregenerate
		| exile
		| gainlife
		| tap
		| untap
		| draw
		| discard
		| loselife
		| dealquantitydamage
		| dealdamage
		| sacrifice
		| regenerate
		| putcounter
		| puttoken
		| become
		| bereduced
		| return_
		| paylife
		| prevention
		| addmana
		| counterspell
) + Optional(quantifier)

oneshot << Optional(subject) + delimitedListAnd(effect)