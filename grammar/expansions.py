from pyparsing import *
from basic import *
from expansions_h import *

frequency << oneOf("M R U C L S")
expcode << (digit|caps) + Optional(digit|caps) + Optional(digit|caps)
expansion << Group(Combine(expcode) + Suppress(DASH) + frequency)
cardexpansions << Group(delimitedList(expansion, COMMA))
