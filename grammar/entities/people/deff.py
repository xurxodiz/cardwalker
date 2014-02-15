from pyparsing import *

from ...constants.people.deff import *
from ...constants.prepositions.deff import UNDER
from ...constants.verbs.deff import CONTROL
from ..articles.deff import det

from decl import *

# we can't include all people possesives here,
# because it would be an infinite recursion loop
your << YOUR
its << ITS
their << THEIR
his << HIS
singleposs << (your|its|their|his)

who << (YOU | IT | THEY | HE | PLAYER | OPPONENT | CONTROLLER | OWNER)

person << Optional(det|singleposs) + who

people << delimitedListAnd(person)

personposs << person + POSS

peopleposs << (personposs|singleposs)
peoplecontrol << people + CONTROL
undercontrol << UNDER + peopleposs + CONTROL