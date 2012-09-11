from pyparsing import *
from basic import *

frequency = or_l("MRUCLS")
expcode = (digit|caps) + Optional(digit|caps) + Optional(digit|caps)
expansion = Group(Group(expcode) + Suppress(DASH) + frequency)
cardexpansions = Group(delimitedList(expansion, COMMA))
