from pyparsing import *

import act

PLUS = Forward()
MINUS = Forward()

XVAR = Forward().setParseAction(act.xvar)

NUM = Forward().setParseAction(act.num)
FULLNUM = Forward().setParseAction(act.fullnum)