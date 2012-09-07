from pyparsing import *
from basic import *

colorname = Or(map(CaselessLiteral, ["white", "blue", "black", "red", "green"]))

noncolorname = CaselessLiteral("non") + colorname

abschar = Or(map(CaselessLiteral, ["colorless", "colored", "multicolored", "monocolored"]))

color = colorname | noncolorname | abschar

manasymbol = Or(map(CaselessLiteral, "WUBRG"))
cardcost = Group(Optional(number) + OneOrMore(manasymbol) | number)