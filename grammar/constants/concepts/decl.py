from pyparsing import *

IT = Forward()
SPELL = Forward()
PERMANENT = Forward()
CARD = Forward()
ABILITY = Forward()
COUNTER = Forward()

concept = Forward()