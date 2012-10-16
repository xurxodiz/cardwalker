from pyparsing import *

import act

noun = Forward()
andnoun = Forward()
ornoun = Forward().setParseAction(act.ornoun)

baseobject_ = Forward().setParseAction(act.baseobject_)

object_ = Forward().setParseAction(act.object_)
orobjects = Forward().setParseAction(act.orobjects)
andobjects = Forward()

it = Forward().setParseAction(act.it)
they = Forward().setParseAction(act.they)

objects = Forward()
