from pyparsing import *

import act

turn = Forward().setParseAction(act.turn)
upkeep = Forward().setParseAction(act.upkeep)
drawstep = Forward().setParseAction(act.drawstep)
precombat = Forward().setParseAction(act.precombat)
combat = Forward().setParseAction(act.combat)
poscombat = Forward().setParseAction(act.poscombat)

step = Forward().setParseAction()

until = Forward().setParseAction(act.until)

havekeywords = Forward().setParseAction(act.havekeywords)
getptmod = Forward().setParseAction(act.getptmod)
beindestructible = Forward().setParseAction(act.beindestructible)
beunblockable = Forward().setParseAction(act.beunblockable)
gaincontrol = Forward().setParseAction(act.gaincontrol)
cantblock = Forward().setParseAction(act.cantblock)
mustattack = Forward().setParseAction(act.mustattack)

#quotedtriggered = Forward().setParseAction(act.quotedtriggered)
#quotedactivated = Forward().setParseAction(act.quotedactivated)
#abilities = Forward().setParseAction(act.abilities)
#gainabilities = Forward().setParseAction(act.gainabilities)

property_ = Forward().setParseAction()

properties = Forward().setParseAction(act.properties)

continuous = Forward().setParseAction(act.continuous)