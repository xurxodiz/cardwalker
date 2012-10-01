from pyparsing import *

turn = Forward()
upkeep = Forward()
drawstep = Forward()
precombat = Forward()
combat = Forward()
poscombat = Forward()

step = Forward()

until = Forward()

havekeywords = Forward()
getptmod = Forward()
beindestructible = Forward()
beunblockable = Forward()
gaincontrol = Forward()
cantblock = Forward()
mustattack = Forward()

#quotedtriggered = Forward()
#quotedactivated = Forward()
#abilities = Forward()
#gainabilities = Forward()

property_ = Forward()

properties = Forward()

continuous = Forward()