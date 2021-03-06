import string

from pyparsing import *
from ..constants.punctuation.deff import DASH, COMMA, EOL
from ..constants.types.deff import FREQUENCY
from decl import *

frequency << FREQUENCY
expcode << Word(string.digits + string.uppercase)

expansion << expcode + Suppress(DASH) + frequency
