from pyparsing import *

import act

until = Forward().setParseAction(act.until)

havekeywords = Forward().setParseAction(act.havekeywords)
getptmod = Forward().setParseAction(act.getptmod)
gaincontrol = Forward().setParseAction(act.gaincontrol)
cantblock = Forward().setParseAction(act.cantblock)
mustattack = Forward().setParseAction(act.mustattack)

property_ = Forward().setParseAction()

#quotedtriggered = Forward().setParseAction(act.quotedtriggered)
#quotedactivated = Forward().setParseAction(act.quotedactivated)
#abilities = Forward().setParseAction(act.abilities)
#gainabilities = Forward().setParseAction(act.gainabilities)

properties = Forward().setParseAction(act.properties)

continuous = Forward().setParseAction(act.continuous)