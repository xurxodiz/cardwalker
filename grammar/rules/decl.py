from pyparsing import *

import act

rule = Forward().setParseAction(act.rule)
reminder = Forward()

rulelist = Forward().setParseAction(act.rulelist)