from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *
from constants import *

det = Group(TARGET
	| Optional(UPTO) + fullnumber + TARGET
	| (THIS|THAT)
	| AN
	| HIS
	| ALL
	| EACH
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

people = Optional(det) + (YOU | PLAYER | OPPONENT)

where = Group(people + CONTROL
		| IN + zone
)

concept = SPELL | PERMANENT | CARD | ABILITY

obj = (Optional(adj)
	+ delimitedListAndOr(subtype | type_ | concept)
	+ Optional(where)
)

objects = Group(delimitedListAndOr(det + obj | obj))

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

properties = (HAVE + delimitedListAndOr(keywords)
			| GET + ptmod
			| BE + indestructible
			| BE + unblockable
)

until = CaselessLiteral("until end of turn")

continuous = objects + delimitedListAndOr(properties) + Optional(until)

condition = Group(CaselessLiteral("enters the battlefield")
		| CaselessLiteral("leaves the battlefield")
		| CaselessLiteral("dies")
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| CaselessLiteral("attacks alone")
)

effect = Group(DESTROY + objects
		| EXILE + objects
		| GAIN + number + LIFE
		| TAP + objects
		| continuous
		| DISCARD + objects + Optional(RANDOM)
		| LOSE + number + LIFE
		| DEAL + number + DAMAGE + TO + objects
		| DEAL + DAMAGE + TO + objects
		| SACRIFICE + objects
) # + Optional(equal|for_)

trigger = condition

triggerer = Optional(THIS) + (objects
	| people
	| (SkipTo(trigger))
)

nonmayer = (objects
	| people
	| IT
	| (cardname + SkipTo(effect))
)
mayer = people + MAY + Optional(nonmayer) 
effecter = (mayer|nonmayer)


intervif = Literal("FILLER")
unless = Literal("FILLER")

trigger_clause = WHEN + triggerer + trigger + Optional(COMMA + intervif)
effect_clause = Optional(effecter) + effect + Optional(unless)

triggered = Group(trigger_clause) + COMMA + Group(effect_clause)

rule = Group(triggered|keywords|continuous|effect_clause) + Optional(POINT)

cardrules = delimitedList(rule, EOL)