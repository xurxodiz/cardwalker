from pyparsing import *

from ..constants.punctuation.deff import LPAREN, RPAREN, POINT, EOL
from keywords.deff import keywords
from continuous.deff import continuous
from oneshot.deff import oneshot

from decl import *

"""

intervif << Literal("FILLER")

condition << ( \
		ENTER + zone + Optional(undercontrol)
		| LEAVE + zone
		| DIE
		| GAIN + LIFE
		| DRAW + objects
		| LOSE + LIFE
		| ATTACK + ALONE
		| people + CONTROL + objects
)n

cost << (TAPSYMBOL | UNTAPSYMBOL | effect | lifepay | manapayment | loyaltycost)

activated << delimitedList(cost) + COLON + (oneshot|continuous)

trigger << condition

when_trigger << WHEN + subject + trigger

trigger_clause << (when_trigger
	| step_time
) + Optional(COMMA + intervif)

triggered << Group(trigger_clause) + COMMA + Group(oneshot|continuous)
"""

rule << (oneshot | triggered | activated | keywords | continuous) + Optional(POINT)

reminder << Suppress(LPAREN + SkipTo(RPAREN) + RPAREN)
rulelist << (OneOrMore(rule) + Optional(reminder) + EOL)

cardrules << OneOrMore(rulelist)