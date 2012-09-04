from pyparsing import *
from basic import *
from types import *

cardname = Group(Word(alphas + " '"))

colorname = Or(map(CaselessLiteral, ["white", "blue", "black", "red", "green"]))
manacolor = Or(map(CaselessLiteral, "WUBRG"))
cardcost = Optional(number) + OneOrMore(manacolor) | number

supertypes = OneOrMore(a_supertype)

types = OneOrMore(a_type)

subtypes = OneOrMore(a_subtype)

cardtypeline = Optional(supertypes) + types + Optional(Suppress(dash) + subtypes)

ptchange = (plus | minus) + number
ptquantity = asterisk | number | (asterisk + ptchange)

cardpt = Group(ptquantity + Suppress(slash) + ptquantity)

keyword = (Or(map(CaselessLiteral, ["Flying",
									"Deathtouch",
									"Trample",
									"Haste",
									"Flash",
									"Vigilance",
									"Intimidate",
									"Exalted",
									"Lifelink", 
									"First strike"]))
		| Group(CaselessLiteral("Protection") + delimitedListAnd(Literal("from") + colorname))
)

reminder = lparen + SkipTo(rparen) + rparen
keywords = delimitedList(keyword+Optional(reminder), comma)


condition = (Literal("enters the battlefield")
		| Literal("dies")
		| Literal("gain life")
		| Literal("gains life")
		| Literal("draw a card")
		| Literal("draws a card")
		| Literal("lose life")
		| Literal("loses life")
)

subject = (Literal("you")
	| Literal("an opponent")
	| Literal("a player")
	| OneOrMore(~condition + cardname)
)

postargets = (a_supertype + a_type
	| a_supertype + a_subtype
	| a_type
	| Literal("player")
	| Literal("opponent")
	| a_subtype
)

targets = Literal("target") + delimitedListOr(postargets)

effect = (Literal("destroy") + targets
		| Literal("gain") + number + Literal("life"))

trigger = Literal("When") + subject + condition + Suppress(comma) + effect + point

continuous = effect

rules = trigger|keywords|continuous
cardrules = ZeroOrMore(rules)

frequency = Or(map(Literal, "MRUCLS"))
expcode = (digit|caps) + (digit|caps) + Optional(digit|caps)
expansion = Group(Group(expcode) + Suppress(dash) + frequency)
cardexpansions = Group(delimitedList(expansion, comma))

card = (cardname
	+ cardcost
	+ cardtypeline
	+ cardpt
	+ cardrules
	+ cardexpansions
)