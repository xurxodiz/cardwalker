from pyparsing import *

import act

triggered = Forward()

intervif = Forward()

condition = Forward()

cost = Forward()
activated = Forward()
trigger = Forward()
when_trigger = Forward()
trigger_clause = Forward()
triggered = Forward()

rule = Forward().setParseAction(act.rule)
reminder = Forward()

rulelist = Forward().setParseAction(act.rulelist)
cardrules = Forward().setParseAction(act.cardrules)