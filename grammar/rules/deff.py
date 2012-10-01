from pyparsing import *

from ..constants.punctuation.deff import LPAREN, RPAREN, POINT, EOL
from keywords.deff import keywords
from continuous.deff import continuous

from decl import *

"""
unless << Literal("FILLER")
intervif << Literal("FILLER")
undercontrol << (UNDER + peopleposs + CONTROL)

condition << ( \
		ENTER + zone + Optional(undercontrol)
		| LEAVE + zone
		| DIE
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| ATTACK + ALONE
		| people + CONTROL + objects
)

lifepay << (PAY + quantity + LIFE)

prevention << (PREVENT + Optional(THE + NEXT) + quantity
		+ DAMAGE + Literal("that would be dealt")
		+ Optional(BY|TO) + objects
		+ FROM + SOURCE + WITH + keywords
)

cantregenerate << subject + CANT + BE + REGENERATE

where << (WHERE + XVAR + BE + Optional(THE+NUMBER+OF) + objects)

equal << (EQUAL + TO + THE + NUMBER + OF + objects)

for_ << (FOR + EACH + objects)

effect << Group( \
		DESTROY + objects + Optional(cantregenerate)
		| EXILE + objects + Optional(Group(FROM + delimitedListAnd(zone)))
		| GAIN + quantity + LIFE
		| TAP + objects
		| UNTAP + objects
		| DRAW + objects
		| DISCARD + objects + Optional(ATRANDOM)
		| LOSE + quantity + LIFE
		| DEAL + quantity + DAMAGE + TO + objects
		| DEAL + DAMAGE + TO + objects
		| SACRIFICE + objects
		| REGENERATE + objects
		| PUT + quantity + ptmod + COUNTER + ON + objects 
		| PUT + Optional(quantity + cardpt) + objects \
			+ Optional(WITH + delimitedListAnd(keywords)) + (INTO|ONTO) + zone
		| BECOME + number # for life totals
		| BE + REDUCE + BY + number
		| RETURN + objects + Optional(FROM + delimitedListAnd(zone)) + TO + zone + Optional(undercontrol)
		| lifepay
		| PAY + manapayment
		| prevention
		| ADD + manapayment + TO + peopleposs + MANA + POOL
		| COUNTER + objects
)
+ Optional( \
	for_
	| COMMA + (where|equal)
)

oneshot << Optional(subject) + delimitedListAnd(effect) + Optional(unless)

cost << (TAPSYMBOL | UNTAPSYMBOL | effect | lifepay | manapayment | loyaltycost)

activated << delimitedList(cost) + COLON + (oneshot|continuous)

trigger << condition

when_trigger << WHEN + subject + trigger

trigger_clause << (when_trigger
	| step_time
) + Optional(COMMA + intervif)

triggered << Group(trigger_clause) + COMMA + Group(oneshot|continuous)
"""

rule << (triggered|activated|keywords|continuous|oneshot) + Optional(POINT)

reminder << Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rulelist << OneOrMore(~EOL + rule) + Optional(reminder)

cardrules << ZeroOrMore(rulelist)