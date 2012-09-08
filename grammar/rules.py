from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *
from constants import *

concept = SPELL | PERMANENT | CARD | ABILITY
people = or_cl (["you", "opponent", "player"])
object_mod = people + CONTROL

obj = (ZeroOrMore(delimitedListAndOr(color))
	+ ZeroOrMore(delimitedListAndOr(nontype))
	+ ZeroOrMore(delimitedListAndOr(supertype))
	+ OneOrMore(delimitedListAndOr(subtype | type_ | concept))
	+ Optional(Group(OneOrMore(object_mod)))
)

objects = Group(AN + obj | obj)

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

continuous = objects + delimitedListAndOr(properties)

condition = Group(CaselessLiteral("enters the battlefield")
		| CaselessLiteral("leaves the battlefield")
		| CaselessLiteral("dies")
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| CaselessLiteral("attacks alone")
)

targets = Optional(UPTO + fullnumber) + TARGET + (people|objects)

until = CaselessLiteral("until end of turn")

effect = Group(DESTROY + Group(delimitedListAndOr(targets))
		| EXILE + Group(delimitedListAndOr(targets))
		| GAIN + number + LIFE
		| TAP + targets
		| continuous + Optional(until)
		| DISCARD + Optional(fullnumber) + objects
)

trigger = condition

triggerer = Optional(THIS) + (objects
	| people
	| (SkipTo(trigger))
)

nonmayer = (objects
	| people
	| targets
	| IT
	| (THIS + objects | THIS + people)
	| (cardname + SkipTo(effect))
)
mayer = (people + MAY | people + MAY + nonmayer) 
effecter = (mayer|nonmayer)


intervif = Literal("FILLER")
unless = Literal("FILLER")

trigger_clause = WHEN + triggerer + trigger + Optional(COMMA + intervif)
effect_clause = Optional(effecter) + effect + Optional(unless)

triggered = Group(trigger_clause) + COMMA + Group(effect_clause)

rule = Group(triggered|keywords|continuous|effect_clause) + Optional(POINT)

cardrules = delimitedList(rule, EOL)