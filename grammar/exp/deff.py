from pyparsing import *

from ..basic.constants.deff import *

from decl import *

frequency << oneOf("M R U C L S")
expcode << Combine(
	(DIGIT|UPPERCASE)
	+ Optional(DIGIT|UPPERCASE)
	+ Optional(DIGIT|UPPERCASE)
)
expansion << expcode + Suppress(DASH) + frequency
cardexpansions << delimitedList(expansion, COMMA)
