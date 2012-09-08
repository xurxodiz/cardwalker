from pyparsing import *
from basic import *

colorname = or_cl(["white", "blue", "black", "red", "green"])

noncolorname = CaselessLiteral("non") + colorname

abschar = or_cl(["colorless", "colored", "multicolored", "monocolored"])

color = colorname | noncolorname | abschar

manasymbol = or_l("WUBRG")
cardcost = Group(Optional(number) + OneOrMore(manasymbol) | number)