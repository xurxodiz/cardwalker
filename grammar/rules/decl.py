from pyparsing import *

import act

tapsymbol = Forward()
untapsymbol = Forward()

cost = Forward()
activated = Forward()

rule = Forward().setParseAction(act.rule)
reminder = Forward()

rulelist = Forward().setParseAction(act.rulelist)