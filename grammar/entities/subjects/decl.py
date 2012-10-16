from pyparsing import *

import act

mayer = Forward().setParseAction(act.mayer)
subject = Forward().setParseAction(act.subject)