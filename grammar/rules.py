from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *
from constants import *

quantity = (number
		| fullnumber
		| UPTO + fullnumber
		| fullnumber
		| AN
		| ANOTHER
)

det = Group(TARGET
	| quantity + TARGET
	| quantity
	| (THIS|THAT)
	| OTHER
	| HIS
	| ALL
	| EACH
	| YOUR
	| ITS
)

people = Group(Optional(det) + (YOU | PLAYER | OPPONENT | CONTROLLER | OWNER))

peopleposs = Group(YOUR
		| people + POSS
)

zone = Group (peopleposs + (GRAVEYARD|HAND|LIBRARY)
		| det + delimitedListAndOr(GRAVEYARD|HAND|LIBRARY)
		| THE + BATTLEFIELD
)

adj = Group(delimitedListAndOr(color | nontype | supertype))

where = Group(people + CONTROL
		| IN + zone
)

concept = SPELL | PERMANENT | CARD | ABILITY

obj = Group(Optional(adj)
	+ delimitedListAndOr(subtype | type_ | concept)
	+ Optional(where)
)

properties = Forward()
condition = Forward()
effect = Forward()
continuous = Forward()

cardname = Group(OneOrMore(~(condition|effect|properties) + Word(alphas + "',")))

objects = Group(delimitedListAndOr(det + obj | obj)
	| IT
	| peopleposs + LIFE + TOTAL
	| cardname
)

peopleres = Group(peopleposs + LIFE + TOTAL
	| peopleposs + HAND + SIZE
)

mayer = people + Optional(MAY + Optional(people|objects))
subject = (peopleres|mayer|people|objects)

protection = Group(PROTECTION + delimitedListAnd(FROM + color))

landwalk = (or_cl (["mountainwalk", "forestwalk", "swampwalk", "islandwalk", "plainswalk"]))

keyword = (or_cl (["Flying",
				"Deathtouch",
				"Trample",
				"Haste",
				"Flash",
				"Vigilance",
				"Intimidate",
				"Exalted",
				"Lifelink", 
				"Hexproof",
				"First strike"])
		| protection
		| landwalk
)

indestructible = CaselessLiteral("indestructible")
unblockable = CaselessLiteral("unblockable")

keywords = delimitedListAnd(keyword)

triggered = Forward()

properties << (HAVE + delimitedListAndOr(keywords)
			| GET + ptmod
			| BE + indestructible
			| BE + unblockable
			| GAIN + delimitedListAnd(keywords | ptmod | (QUOTE + triggered + QUOTE))
			| GAIN + CONTROL + OF + objects
			| CANT + BLOCK
			| MUST + ATTACK
)

step = (TURN|UPKEEP|DRAWSTEP|PRECOMBAT|COMBAT|POSCOMBAT|TURN)
step_time = Optional(AT + THE) + (BEGINNING|END) + OF + (peopleposs + step|step)
until = UNTIL + step_time

continuous << Optional(subject) +  delimitedListAnd(properties) + Optional(until) + Optional(unless)

condition << Group(ENTER + zone
		| LEAVE + zone
		| DIE
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| ATTACK + ALONE
		| people + CONTROL + objects
)

effect << Group(DESTROY + objects
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
		| PAY + quantity + LIFE
		| PUT + quantity + ptmod + COUNTER + ON + objects 
		| PUT + quantity + cardpt + objects + Optional(WITH + delimitedListAnd(keywords)) + ONTO + zone
		| BECOME + number # for life totals
		| BE + REDUCED + BY + number
		| RETURN + objects + Optional(FROM + delimitedListAnd(zone)) + TO + zone
) # + Optional(equal|for_)

trigger = condition

intervif = Literal("FILLER")
unless = Literal("FILLER")

when_trigger = WHEN + subject + trigger

trigger_clause = (when_trigger
	| step_time
) + Optional(COMMA + intervif)

oneshot = Optional(subject) + delimitedListAnd(effect) + Optional(unless)

triggered = Group(trigger_clause) + COMMA + Group(oneshot|continuous)

reminder = Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rule = Group(triggered|keywords|continuous|oneshot) + Optional(POINT) + Optional(reminder)

cardrules = delimitedList(rule, Optional(EOL))