from pyparsing import *

from ..constants.punctuation.deff import LPAREN, RPAREN, POINT, EOL
from triggered.deff import triggered
from keywords.deff import keywords
from continuous.deff import continuous
from oneshot.deff import oneshot

from decl import *

"""
cost << (TAPSYMBOL | UNTAPSYMBOL | effect | lifepay | manapayment | loyaltycost)
activated << delimitedList(cost) + COLON + (oneshot|continuous)
"""

rule << (oneshot | triggered | keywords | continuous) + Optional(POINT)

reminder << Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rulelist << OneOrMore(rule) + Optional(reminder)