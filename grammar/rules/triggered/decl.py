from pyparsing import *

enterzone = Forward()
leavezone = Forward()
die = Forward()
gainlife = Forward()
drawcards = Forward()
loselife = Forward()
attackalone = Forward()
controlobjects = Forward()

trigger = Forward()

when_trigger = Forward()
at_trigger = Forward()
trigger = Forward()

intervif = Forward()

trigger_clause = Forward()
triggered = Forward()