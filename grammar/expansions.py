from pyparsing import *
from basic import *

frequency = Or(map(Literal, "MRUCLS"))
expcode = (digit|caps) + (digit|caps) + Optional(digit|caps)
expansion = Group(Group(expcode) + Suppress(dash) + frequency)
cardexpansions = Group(delimitedList(expansion, comma))
