from pyparsing import *

import act

frequency = Forward().setParseAction(act.frequency)
expcode = Forward().setParseAction(act.expcode)
expansion = Forward().setParseAction(act.expansion)
cardexpansions = Forward().setParseAction(act.cardexpansions)