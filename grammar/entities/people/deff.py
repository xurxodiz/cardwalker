from pyparsing import *

from ...constants.people.deff import *
from ...constants.prepositions.deff import UNDER
from ...constants.verbs.deff import CONTROL
from ..articles.deff import det

from decl import *

detpeople << (det|YOUR) + (PLAYER | OPPONENT | CONTROLLER | OWNER)

people << delimitedListAnd(detpeople|YOU)

your << YOUR
their << THEIR
his << HIS
peoploss << people + POSS

peopleposs << (your|their|his|peoploss)
peoplecontrol << people + CONTROL
undercontrol << UNDER + peopleposs + CONTROL