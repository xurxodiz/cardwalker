from pyparsing import *

BEGINNING = Forward()
END = Forward()

TURN = Forward()
UPKEEP = Forward()
DRAWSTEP = Forward()
PRECOMBAT = Forward()
COMBAT = Forward()
POSCOMBAT = Forward()