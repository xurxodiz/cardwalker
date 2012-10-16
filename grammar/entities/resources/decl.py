from pyparsing import *

import act

lifetotal = Forward().setParseAction(act.lifetotal)
handsize = Forward().setParseAction(act.handsize)

resource = Forward()