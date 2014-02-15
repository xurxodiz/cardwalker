from pyparsing import *

import act

SPELL = Forward()
PERMANENT = Forward()
CARD = Forward()

THISCARD = Forward()

COUNTER = Forward()