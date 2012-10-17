from pyparsing import *

import act

SPELL = Forward()
PERMANENT = Forward()
CARD = Forward()

COUNTER = Forward()