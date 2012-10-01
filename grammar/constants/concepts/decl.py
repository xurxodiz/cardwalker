from pyparsing import *

import act

IT = Forward()
SPELL = Forward()
PERMANENT = Forward()
CARD = Forward()
ABILITY = Forward()
COUNTER = Forward()

concept = Forward().setParseAction(act.concept)