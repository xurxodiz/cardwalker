from pyparsing import *

import act

your = Forward().setParseAction(act.your)
its = Forward().setParseAction(act.its)
their = Forward().setParseAction(act.their)
his = Forward().setParseAction(act.his)
singleposs = Forward().setParseAction(act.singleposs)

who = Forward().setParseAction(act.who)

person = Forward().setParseAction(act.person)
people = Forward().setParseAction(act.people)

personposs = Forward().setParseAction(act.personposs)
peopleposs = Forward()

peoplecontrol = Forward().setParseAction(act.peoplecontrol)
undercontrol = Forward().setParseAction(act.undercontrol)