from pyparsing import *

import act

quantity = Forward()
det = Forward()

people = Forward()
peopleposs = Forward()

zone = Forward()

adj = Forward()

undercontrol = Forward()
where = Forward()

concept = Forward()

obj = Forward()
properties = Forward()
condition = Forward()

objects = Forward()

peopleres = Forward()
mayer = Forward()
subject = Forward()

triggered = Forward()
properties = Forward()

step = Forward()
step_time = Forward()

until = Forward()
intervif = Forward()
unless = Forward()

condition = Forward()
lifepay = Forward()
prevention = Forward()
cantregenerate = Forward()

equal = Forward()
for_ = Forward()

effect = Forward()
continuous = Forward()
oneshot = Forward()

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