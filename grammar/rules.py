from pyparsing import *
from basic import *
from types import *
from mana import *
from pt import *

people = or_cl (["you", "an opponent", "a player"])
control = or_cl (["control", "controls"])
object_mod = people + control

objects = Group(ZeroOrMore(delimitedListAndOr(a_color))
	+ ZeroOrMore(delimitedListAndOr(a_nontype))
	+ ZeroOrMore(delimitedListAndOr(a_supertype))
	+ OneOrMore(delimitedListAndOr(a_subtype | a_type | a_concept))
	+ ZeroOrMore(object_mod)
)

how_many = (Optional(CaselessLiteral("up to")) + fullnumber
			| CaselessLiteral("all")
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
		| Group(CaselessLiteral("Protection") + delimitedListAnd(from_ + a_color))
)

indestructible = CaselessLiteral("indestructible")
unblockable = CaselessLiteral("unblockable")

reminder = Suppress(lparen + SkipTo(rparen) + rparen)
keywords = delimitedListAnd(keyword+Optional(reminder))


condition = (CaselessLiteral("enters the battlefield")
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

subject = (people
	| an + objects + object_mod
	| (SkipTo(condition))
)


postargets = (or_cl (["player", "opponent"])
			| objects
)

targets = (CaselessLiteral("target") + postargets
		| how_many	+ Literal("target") + postargets
)

effect = (CaselessLiteral("destroy") + delimitedListAndOr(targets)
		| CaselessLiteral("gain") + number + CaselessLiteral("life")
		| CaselessLiteral("tap") + targets
)

may_effect = Optional(people + Optional("may")) + effect

trigger = when + Group(subject) + Group(condition)  + comma + Group(may_effect) 

properties = (have + delimitedListAndOr(keywords)
			| get + ptmod
			| are + indestructible
			| are + unblockable
)

continuous = objects + Optional(object_mod) + delimitedListAndOr(properties)

rules = Group(trigger|keywords|continuous|may_effect) + Optional(point)
cardrules = ZeroOrMore(rules)