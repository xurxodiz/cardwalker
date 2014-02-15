from pyparsing import *

from ..constants.punctuation.deff import COLON, LPAREN, RPAREN, LBRACE, RBRACE, POINT, EOL
from ..constants.resources.deff import TAPSYMBOL, UNTAPSYMBOL
from ..mana.deff import manapayment
from ..ptl.deff import loyaltymod
from triggered.deff import triggered
from keywords.deff import keywords
from continuous.deff import continuous
from oneshot.deff import oneshot, effect

from decl import *

tapsymbol << LBRACE + TAPSYMBOL + RBRACE
untapsymbol << LBRACE + UNTAPSYMBOL + RBRACE

cost << (tapsymbol | untapsymbol | effect | manapayment | loyaltymod)
activated << delimitedList(cost) + COLON + (oneshot|continuous)

# continuous has to come before keywords
# or "enchanted creature" (e.g.) creates a ENCHANT token
rule << (continuous | oneshot | triggered | activated | keywords) + Optional(POINT)

reminder << Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rulelist << OneOrMore(rule) + Optional(reminder)