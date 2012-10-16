from pyparsing import *

import act

detpeople = Forward().setParseAction(act.detpeople)
people = Forward().setParseAction(act.people)

your = Forward().setParseAction(act.your)
their = Forward().setParseAction(act.their)
his = Forward().setParseAction(act.his)
peoploss = Forward().setParseAction(act.peoploss)

peopleposs = Forward().setParseAction(act.peopleposs)
peoplecontrol = Forward().setParseAction(act.peoplecontrol)
undercontrol = Forward().setParseAction(act.undercontrol)