from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *

people = or_cl (["you", "opponent", "player"])
control = or_cl (["control", "controls"])
object_mod = people + control

objects = Group(ZeroOrMore(delimitedListAndOr(color))
	+ ZeroOrMore(delimitedListAndOr(nontype))
	+ ZeroOrMore(delimitedListAndOr(supertype))
	+ OneOrMore(delimitedListAndOr(subtype | type_ | concept))
	+ Optional(Group(OneOrMore(object_mod)))
)
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
		| Group(CaselessLiteral("Protection") + delimitedListAnd(from_ + color))
)

indestructible = CaselessLiteral("indestructible")
unblockable = CaselessLiteral("unblockable")

reminder = Suppress(lparen + SkipTo(rparen) + rparen)
keywords = delimitedListAnd(keyword+Optional(reminder))

properties = (have + delimitedListAndOr(keywords)
			| get + ptmod
			| are + indestructible
			| are + unblockable
)

continuous = objects + delimitedListAndOr(properties)

condition = Group(CaselessLiteral("enters the battlefield")
		| CaselessLiteral("leaves the battlefield")
		| CaselessLiteral("dies")
		| CaselessLiteral("gain life")
		| CaselessLiteral("gains life")
		| CaselessLiteral("draw a card")
		| CaselessLiteral("draws a card")
		| CaselessLiteral("lose life")
		| CaselessLiteral("loses life")
		| CaselessLiteral("attacks alone")
)

targets = Optional(UPTO + fullnumber) + target + (people|objects)

until = CaselessLiteral("until end of turn")

effect = Group(CaselessLiteral("destroy") + Group(delimitedListAndOr(targets))
		| CaselessLiteral("gain") + number + CaselessLiteral("life")
		| CaselessLiteral("tap") + targets
		| continuous + Optional(until)
)

trigger = condition

triggerer = Optional(this) + (objects
	| people
	| (SkipTo(trigger))
)

nonmayer = (objects
	| people
	| targets
	| CaselessLiteral("it")
	| (this + objects | this + people)
	| (cardname + SkipTo(effect))
)
mayer = (people + MAY | people + MAY + nonmayer) 
effecter = (mayer|nonmayer)


intervif = Literal("FILLER")
unless = Literal("FILLER")

trigger_clause = when + triggerer + trigger + Optional(comma + intervif)
effect_clause = Optional(effecter) + effect + Optional(unless)

triggered = Group(trigger_clause) + comma + Group(effect_clause)

rule = Group(triggered|keywords|continuous|effect_clause) + Optional(point)

cardrules = delimitedList(rule, EOL)