from pyparsing import *
from basic import *

a_colorname = Or(map(CaselessLiteral, ["white", "blue", "black", "red", "green"]))

a_noncolorname = CaselessLiteral("non") + a_colorname

an_abschar = Or(map(CaselessLiteral, ["colorless", "colored", "multicolored", "monocolored"]))

a_color = a_colorname | a_noncolorname | an_abschar

manacolor = Or(map(CaselessLiteral, "WUBRG"))
cardcost = Group(Optional(number) + OneOrMore(manacolor) | number)