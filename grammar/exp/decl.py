from pyparsing import *

import act

frequency = Forward()
expcode = Forward()
expansion = Forward().setParseAction(act.expansions)
cardexpansions = Forward().setParseAction(act.cardexpansions)