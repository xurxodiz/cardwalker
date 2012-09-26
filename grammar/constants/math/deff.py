from pyparsing import *

import string
from decl import *
from ...functions.deff import *

PLUS << Literal("+")
MINUS << Literal("-")

XVAR << (Literal("X") | Literal("*"))

NUM << Word(string.digits)
FULLNUM << oneOfNamed ("one two three four five six seven eight nine")