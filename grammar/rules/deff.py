"""from pyparsing import *
from mana import *
from basic import *
from types import *
from pt import *

quantity << ( \
		NUM
		| XVAR
		| XVAR + NUM
		| FULLNUM
		| UPTO + FULLNUM
		| AN
		| ANOTHER
		| ALL
)

det << Group( \
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

people << Group(Optional(det) + (YOU | PLAYER | OPPONENT | CONTROLLER | OWNER))

peopleposs << Group(YOUR
		| THEIR
		| HIS
		| people + POSS
)

zone << Group ( \
		peopleposs + (GRAVEYARD|HAND|LIBRARY)
		| det + delimitedListAndOr(GRAVEYARD|HAND|LIBRARY)
		| THE + BATTLEFIELD 
		| THE + TOP + OF + peopleposs + LIBRARY
)

adj << Group(delimitedListAndOr( \
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

where << Group(people + CONTROL
		| IN + zone
		| OF + zone
		| FROM + zone
)

concept << (SPELL | PERMANENT | CARD | ABILITY)

obj << Group(Optional(adj)
	+ delimitedListAndOr(subtype | type_ | concept)
	+ Optional(where)
)

properties << Forward()
condition << Forward()
effect << Forward()
continuous << Forward()

cardname << Group(OneOrMore(~(condition|effect|properties|FROM) + Word(alphas + "',")))

objects << Group(\
	delimitedListAndOr(det + obj | obj)
	| IT
	| peopleposs + LIFE + TOTAL
	| det + TOP + fullnumber + CARD + OF + zone
	| cardname
)

peopleres << Group( \
	peopleposs + LIFE + TOTAL
	| peopleposs + HAND + SIZE
)

mayer << people + Optional(MAY + Optional(people|objects))
subject << (peopleres|mayer|people|objects)

triggered << Forward()

properties << (\
			HAVE + delimitedListAndOr(keywords)
			| GET + ptmod
			| BE + INDESTRUCTIBLE
			| BE + UNBLOCKABLE
			| GAIN + delimitedListAnd(keywords | ptmod | (QUOTE + triggered + QUOTE))
			| GAIN + CONTROL + OF + objects
			| CANT + BLOCK
			| MUST + ATTACK
)

step << (TURN|UPKEEP|DRAWSTEP|PRECOMBAT|COMBAT|POSCOMBAT|TURN)
step_time << Optional(AT + THE) + (BEGINNING|END) + OF + (peopleposs + step|step)
until << UNTIL + step_time

intervif << Literal("FILLER")
unless << Literal("FILLER")
undercontrol << Group( \
			UNDER + peopleposs + CONTROL
)

continuous << Optional(subject) +  delimitedListAnd(properties) + Optional(until) + Optional(unless)

condition << Group( \
		ENTER + zone + Optional(undercontrol)
		| LEAVE + zone
		| DIE
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| ATTACK + ALONE
		| people + CONTROL + objects
)

lifepay << PAY + quantity + LIFE

prevention << (PREVENT + Optional(THE + NEXT) + quantity
		+ DAMAGE + Literal("that would be dealt")
		+ Optional(BY|TO) + objects
		+ FROM + SOURCE + WITH + keywords
)

cantregenerate << subject + CANT + BE + REGENERATE

where << ( \
	WHERE + XVAR + BE + Optional(THE+NUMBER+OF) + objects
)

equal << ( \
	EQUAL + TO + THE + NUMBER + OF + objects
)

for_ << ( \
	FOR + EACH + objects
)

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
		| PUT + Optional(quantity + cardpt) + objects + Optional(WITH + delimitedListAnd(keywords)) + (INTO|ONTO) + zone
		| BECOME + number # for life totals
		| BE + REDUCE + BY + number
		| RETURN + objects + Optional(FROM + delimitedListAnd(zone)) + TO + zone + Optional(undercontrol)
		| lifepay
		| PAY + manapayment
		| prevention
		| ADD + manapayment + TO + peopleposs + MANA + POOL
		| COUNTER + objects
) + Optional( \
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

reminder << Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rule << Group(triggered|activated|keywords|continuous|oneshot) + Optional(POINT) + Optional(reminder)

cardrules << delimitedList(rule, Optional(EOL))
"""