from pyparsing import *

digit = Or(map(Literal, "0123456789"))
caps = Or(map(Literal,"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
nl = Optional(Literal("\r")) + Literal("\n")
dash = Literal("--")

name = Word(alphas + "'" + " ")

manacolor = Or(map(CaselessLiteral, "WUBRG"))
cost = (ZeroOrMore(digit) + OneOrMore(manacolor)) | OneOrMore(digit)


supertype = Or(map(CaselessLiteral, ["Basic", "Legendary", "Snow", "World"]))
supertypes = OneOrMore(supertype)

typ = Or(map(CaselessLiteral, ["Creature", "Tribal", "Instant", "Sorcery", "Artifact", "Enchantment", "Planeswalker"]))
types = OneOrMore(typ)

subtype = Word(alphas + "'")
subtypes = OneOrMore(subtype)

typeline = Optional(supertypes) + types + Optional(Suppress(dash) + subtypes)

pt = Group(OneOrMore(digit) + Suppress("/") + OneOrMore(digit))

ability = CaselessLiteral("Flying") | Group(CaselessLiteral("Protection from") + Or(map(Literal, ["white", "blue", "black", "red", "green"])))
rulestext = Group(delimitedList(ability, ','))

frequency = Or(map(Literal, "MRUCLS"))
expcode = (digit|caps) + (digit|caps) + Optional(digit|caps)
expansion = Group(Group(expcode) + Suppress("-") + frequency)
expansions = Group(delimitedList(expansion, ","))

card = name + cost + typeline + pt + rulestext + expansions