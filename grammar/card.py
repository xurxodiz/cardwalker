from pyparsing import *
from types import *

digit = Or(map(Literal, "0123456789"))
caps = Or(map(Literal,"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

number = OneOrMore(digit)

apostrophe = Literal("'")
asterisk = Literal("*")
plus = Literal("+")
minus = Literal("-")
comma = Literal(",")
point = Literal(".")
lparen = Literal("(")
rparen = Literal(")")
slash = Literal("/")
dash = Word("-")

cardnameword = Word(alphas + "'")
name = Group(OneOrMore(cardnameword))

colorname = Or(map(CaselessLiteral, ["white", "blue", "black", "red", "green"]))
manacolor = Or(map(CaselessLiteral, "WUBRG"))
cost = (Optional(number) + OneOrMore(manacolor)) | number

supertypes = OneOrMore(a_supertype)

types = OneOrMore(a_type)

subtypes = OneOrMore(a_subtype)

typeline = Optional(supertypes) + types + Optional(Suppress(dash) + subtypes)

ptchange = (plus | minus) + number
ptquantity = asterisk | number | (asterisk + ptchange)

pt = Group(ptquantity + Suppress(slash) + ptquantity)

keyword = Or(map(CaselessLiteral, ["Flying", \
									"Deathtouch", \
									"Trample", \
									"Haste", \
									"Flash", \
									"Intimidate", \
									"Exalted", \
									"First strike"])) \
		| Group(CaselessLiteral("Protection from") + colorname)

reminder = lparen + SkipTo(rparen) + rparen
keywords = delimitedList(keyword+Optional(reminder), comma)


condition = (Literal("enters the battlefield")
		| Literal("dies") \
		| Literal("gain life") \
		| Literal("gains life") \
		| Literal("draw a card") \
		| Literal("draws a card") \
		| Literal("lose life") \
		| Literal("loses life")
)

subject = (Literal("you")
	| Literal("an opponent")
	| Literal("a player")
	| OneOrMore(~condition + cardnameword)
)

postargets = (a_supertype + a_type
	| a_supertype + a_subtype
	| a_type
	| Literal("player")
	| Literal("opponent")
	| a_subtype
)

junctargets = (Literal("or") + postargets) | postargets

targets = Literal("target") + delimitedList(junctargets, comma)

effect = (Literal("destroy") + targets
		| Literal("gain") + number + Literal("life"))

trigger = Literal("When") + subject + condition + Suppress(comma) + effect + point

rules = trigger|keywords
rulestext = ZeroOrMore(rules)

frequency = Or(map(Literal, "MRUCLS"))
expcode = (digit|caps) + (digit|caps) + Optional(digit|caps)
expansion = Group(Group(expcode) + Suppress(dash) + frequency)
expansions = Group(delimitedList(expansion, comma))

card = name + cost + typeline + pt + rulestext + expansions