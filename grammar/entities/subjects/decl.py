from pyparsing import *

import act

andobjects = Forward()
orobjects = Forward().setParseAction(act.orobjects)
objects = Forward().setParseAction(act.objects)

mayhave = Forward().setParseAction(act.mayhave)
may = Forward().setParseAction(act.may)
subjects = Forward().setParseAction(act.subjects)