from pyparsing import *

import act

change = Forward().setParseAction(act.change)
amount = Forward().setParseAction(act.amount)

uptoamount = Forward().setParseAction(act.uptoamount)
an = Forward().setParseAction(act.an)
another = Forward().setParseAction(act.another)
alll = Forward().setParseAction(act.alll)

quantity = Forward()

target = Forward().setParseAction(act.target)
quantitytarget = Forward().setParseAction(act.quantitytarget)
this = Forward().setParseAction(act.this)
that = Forward().setParseAction(act.that)
other = Forward().setParseAction(act.other)
each = Forward().setParseAction(act.each)
its = Forward().setParseAction(act.its)
the = Forward().setParseAction(act.the)

det = Forward().setParseAction(act.det)

globaldet = Forward()

detpeople = Forward().setParseAction(act.detpeople)
people = Forward().setParseAction(act.people)

your = Forward().setParseAction(act.your)
their = Forward().setParseAction(act.their)
his = Forward().setParseAction(act.his)
peoploss = Forward().setParseAction(act.peoploss)

peopleposs = Forward().setParseAction(act.peopleposs)

detzone = Forward().setParseAction(act.detzone)
thebattlefield = Forward().setParseAction(act.thebattlefield)
thetopbottomoflibrary = Forward().setParseAction(act.thetopbottomoflibrary)

zone = Forward().setParseAction(act.zone)

peoplecontrol = Forward().setParseAction(act.peoplecontrol)
inzone = Forward().setParseAction(act.inzone)
ofzone = Forward().setParseAction(act.ofzone)
fromzone = Forward().setParseAction(act.fromzone)

where = Forward()

lifetotal = Forward().setParseAction(act.lifetotal)
handsize = Forward().setParseAction(act.handsize)

resource = Forward()

topnum = Forward().setParseAction(act.topnum)

tapped = Forward().setParseAction(act.tapped)
untapped = Forward().setParseAction(act.untapped)
enchanted = Forward().setParseAction(act.enchanted)
equipped = Forward().setParseAction(act.equipped)
exiled = Forward().setParseAction(act.exiled)
sacrificed = Forward().setParseAction(act.sacrificed)
haunted = Forward().setParseAction(act.haunted)

adjective = Forward()

andadjectives = Forward()
oradjectives = Forward().setParseAction(act.oradjectives)
consadjectives = Forward()

adjectives = Forward().setParseAction(act.adjectives)

noun = Forward()
andnoun = Forward()
ornoun = Forward().setParseAction(act.ornoun)
consnoun = Forward()

baseobject_ = Forward().setParseAction(act.baseobject_)

object_ = Forward().setParseAction(act.object_)
orobjects = Forward().setParseAction(act.orobjects)
andobjects = Forward()
consobjects = Forward()
detobjects = Forward()
anddetobjects = Forward()
ordetobjects = Forward().setParseAction(act.ordetobjects)
consdetobjects = Forward()

it = Forward().setParseAction(act.it)
they = Forward().setParseAction(act.they)

objects = Forward()

mayer = Forward().setParseAction(act.mayer)
subject = Forward().setParseAction(act.subject)