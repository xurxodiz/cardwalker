from pyparsing import *

import act

tapsymbol = Forward().setParseAction(act.tapsymbol)
untapsymbol = Forward().setParseAction(act.untapsymbol)

cost = Forward().setParseAction(act.cost)
activated = Forward().setParseAction(act.activated)

rule = Forward().setParseAction(act.rule)
reminder = Forward()

rulelist = Forward().setParseAction(act.rulelist)