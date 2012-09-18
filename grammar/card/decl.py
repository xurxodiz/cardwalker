from pyparsing import *

import act

card = Forward().setParseAction(act.card)