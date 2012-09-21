import string

from pyparsing import *

from ..basic.constants.deff import *

from decl import *

frequency << oneOf("M R U C L S")
expcode << Word(string.digits + string.uppercase)

expansion << expcode + Suppress(DASH) + frequency
cardexpansions << delimitedList(expansion, COMMA)
