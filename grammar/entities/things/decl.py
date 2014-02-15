from pyparsing import *

import act

name = Forward().setParseAction(act.name)
thiscard = Forward().setParseAction(act.thiscard)

named = Forward().setParseAction(act.named)

concept = Forward().setParseAction(act.concept)

noun = Forward()
andnoun = Forward()
ornoun = Forward().setParseAction(act.ornoun)

basething = Forward().setParseAction(act.basething)

thing = Forward().setParseAction(act.thing)
orthings = Forward().setParseAction(act.orthings)
andthings = Forward()

it = Forward().setParseAction(act.it)
they = Forward().setParseAction(act.they)

things = Forward()
