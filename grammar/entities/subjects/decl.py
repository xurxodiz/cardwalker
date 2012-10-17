from pyparsing import *

import act

objects = Forward().setParseAction(act.objects)
mayhave = Forward().setParseAction(act.mayhave)
may = Forward().setParseAction(act.may)
subjects = Forward().setParseAction(act.subjects)