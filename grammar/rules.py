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
)

det = Group(TARGET
	| quantity + TARGET
	| quantity
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

until = CaselessLiteral("until end of turn")

continuous << Optional(subject) +  delimitedListAnd(properties) + Optional(until)

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
		| PUT + (quantity|AN|ANOTHER) + ptmod + COUNTER + ON + objects 
) # + Optional(equal|for_)

trigger = condition

intervif = Literal("FILLER")
unless = Literal("FILLER")

trigger_clause = WHEN + subject + trigger + Optional(COMMA + intervif)
oneshot = Optional(subject) + delimitedListAnd(effect) + Optional(unless)

triggered = Group(trigger_clause) + COMMA + Group(oneshot|continuous)

reminder = Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rule = Group(triggered|keywords|continuous|oneshot) + Optional(POINT) + Optional(reminder)

cardrules = delimitedList(rule, EOL)