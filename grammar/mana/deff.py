from pyparsing import *

from ..constants.resources.deff import *
from ..constants.punctuation.deff import LBRACE, RBRACE, LPAREN, RPAREN, SLASH, EOL
from ..constants.math.deff import NUM, XVAR
from ..constants.modifiers.deff import NON

from decl import *

colorname << COLORNAME
noncolorname << NON + COLORNAME
colorfeature << COLORFEATURE
color << (colorname | noncolorname | colorfeature)

manasymbol << MANASYMBOL
tapsymbol << LBRACE + TAPSYMBOL + RBRACE
untapsymbol << LBRACE + UNTAPSYMBOL + RBRACE
snowsymbol << SNOWSYMBOL

physymbol << LPAREN + manasymbol + SLASH + PHYSYMBOL + RPAREN
hybsymbol << LPAREN + NUM + SLASH + manasymbol + RPAREN
chybsymbol << LPAREN + manasymbol + SLASH + manasymbol + RPAREN

numcost << NUM
xcost << XVAR

singlecost << (numcost|xcost|manasymbol|snowsymbol|physymbol|hybsymbol|chybsymbol)
manapayment << OneOrMore(LBRACE + singlecost + RBRACE)