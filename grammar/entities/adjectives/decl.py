from pyparsing import *

import act

topnum = Forward().setParseAction(act.topnum)

attacking = Forward().setParseAction(act.attacking)
blocking = Forward().setParseAction(act.blocking)
tapped = Forward().setParseAction(act.tapped)
untapped = Forward().setParseAction(act.untapped)
enchanted = Forward().setParseAction(act.enchanted)
equipped = Forward().setParseAction(act.equipped)
exiled = Forward().setParseAction(act.exiled)
sacrificed = Forward().setParseAction(act.sacrificed)
haunted = Forward().setParseAction(act.haunted)

adjective = Forward()

andadjectives = Forward()
oradjectives = Forward().setParseAction(act.oradjectives)

adjectives = Forward().setParseAction(act.adjectives)