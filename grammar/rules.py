from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *
from constants import *

det = Group(TARGET
	| UPTO + fullnumber + TARGET
	| fullnumber + TARGET
	| fullnumber
	| (THIS|THAT)
	| AN
	| OTHER
	| ANOTHER
	| HIS
	| ALL
	| EACH
	| YOUR
)

peopleposs = Group(YOUR
		| det + PLAYER + POSS
		| det + OPPONENT + POSS
		| det
)

zone = Group (peopleposs + (GRAVEYARD|HAND|LIBRARY)
		| THE + BATTLEFIELD
)

adj = Group(delimitedListAndOr(color | nontype | supertype))

people = Group(Optional(det) + (YOU | PLAYER | OPPONENT))

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
	| cardname
)

mayer = people + Optional(MAY + Optional(people|objects))
subject = (mayer|people|objects)

keyword = (or_cl (["Flying",
				"Deathtouch",
				"Trample",
				"Haste",
				"Flash",
				"Vigilance",
				"Intimidate",
				"Exalted",
				"Lifelink", 
				"First strike"])
		| Group(CaselessLiteral("Protection") + delimitedListAnd(FROM + color))
)

indestructible = CaselessLiteral("indestructible")
unblockable = CaselessLiteral("unblockable")

reminder = Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
keywords = delimitedListAnd(keyword+Optional(reminder))

properties << (HAVE + delimitedListAndOr(keywords)
			| GET + ptmod
			| BE + indestructible
			| BE + unblockable
)

until = CaselessLiteral("until end of turn")

continuous << subject +  delimitedListAndOr(properties) + Optional(until)

condition << Group(CaselessLiteral("enters the battlefield")
		| CaselessLiteral("leaves the battlefield")
		| CaselessLiteral("dies")
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| CaselessLiteral("attacks alone")
)

effect << Group(DESTROY + objects
		| EXILE + objects
		| GAIN + number + LIFE
		| TAP + objects
		| DRAW + objects
		| DISCARD + objects + Optional(ATRANDOM)
		| LOSE + number + LIFE
		| DEAL + number + DAMAGE + TO + objects
		| DEAL + DAMAGE + TO + objects
		| SACRIFICE + objects
		| PAY + number + LIFE
) # + Optional(equal|for_)

trigger = condition

intervif = Literal("FILLER")
unless = Literal("FILLER")

trigger_clause = WHEN + subject + trigger + Optional(COMMA + intervif)
oneshot = Optional(subject) + delimitedListAnd(effect) + Optional(unless)

triggered = Group(trigger_clause) + COMMA + Group(oneshot|continuous)

rule = Group(triggered|keywords|continuous|oneshot) + Optional(POINT)

cardrules = delimitedList(rule, EOL)