from pyparsing import *
from basic import *

colorname = or_cl(["white", "blue", "black", "red", "green"])

noncolorname = CaselessLiteral("non") + colorname

abschar = or_cl(["colorless", "colored", "multicolored", "monocolored"])

color = colorname | noncolorname | abschar

manasymbol = or_cl("WUBRG")

TAPSYMBOL = LBRACE + CaselessLiteral("T") + RBRACE
UNTAPSYMBOL = LBRACE + CaselessLiteral("Q") + RBRACE

SNOWSYMBOL = CaselessLiteral("S") 
XVAR = CaselessLiteral("X")

physymbol = LPAREN + manasymbol + SLASH + Literal("p") + RPAREN
chybsymbol = LPAREN + Literal("2") + SLASH + manasymbol + RPAREN
hybsymbol = LPAREN + manasymbol + SLASH + manasymbol + RPAREN

singlecost = (number|manasymbol|physymbol|hybsymbol|chybsymbol|SNOWSYMBOL|XVAR)

manapayment = Group(OneOrMore(LBRACE + singlecost + RBRACE))

cardcost = Group(OneOrMore(singlecost))