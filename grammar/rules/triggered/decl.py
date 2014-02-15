from pyparsing import *

import act

enterzone = Forward()
leavezone = Forward()
die = Forward()
gainlife = Forward()
drawcards = Forward()
loselife = Forward()
attackalone = Forward()
controlobjects = Forward()

trigger_action = Forward()

when_trigger = Forward()

turn = Forward().setParseAction(act.turn)
upkeep = Forward().setParseAction(act.upkeep)
drawstep = Forward().setParseAction(act.drawstep)
precombat = Forward().setParseAction(act.precombat)
combat = Forward().setParseAction(act.combat)
poscombat = Forward().setParseAction(act.poscombat)

step = Forward().setParseAction()

at_trigger = Forward()
trigger = Forward()

intervif = Forward()

trigger_clause = Forward()
triggered = Forward()