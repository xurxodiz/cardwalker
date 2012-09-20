from pyparsing import *

from ..basic.constants.deff import *

from decl import *

colorname << oneOf("white blue black red green", caseless=True)
noncolorname << NON + colorname
abschar << oneOf ("colorless colored multicolored monocolored", caseless=True)
color << (colorname | noncolorname | abschar)

manasymbol << oneOf("W U B R G", caseless=True)
tapsymbol << LBRACE + CaselessLiteral("T") + RBRACE
untapsymbol << LBRACE + CaselessLiteral("Q") + RBRACE
snowsymbol << CaselessLiteral("S")

phyletter << (Suppress("p") | Suppress("P"))
physymbol << LPAREN + manasymbol + SLASH + phyletter + RPAREN
hybsymbol << LPAREN + NUM + SLASH + manasymbol + RPAREN
chybsymbol << LPAREN + manasymbol + SLASH + manasymbol + RPAREN

numcost << NUM
xcost << XVAR

singlecost << (numcost|xcost|snowsymbol|manasymbol|physymbol|hybsymbol|chybsymbol)
manapayment << OneOrMore(LBRACE + singlecost + RBRACE)

nocost << Empty()
docost << OneOrMore(singlecost)

cardcost << (docost + EOL| nocost)