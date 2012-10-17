from pyparsing import *

import act

cardname = Forward()

cardcost = Forward().setParseAction(act.cardcost)

cardsupertypes = Forward().setParseAction(act.cardsupertypes)
cardtypes = Forward().setParseAction(act.cardtypes)
cardsubtypes = Forward().setParseAction(act.cardsubtypes)

cardtypeline = Forward().setParseAction(act.cardtypeline)

cardptl = Forward()

cardrules = Forward().setParseAction(act.cardrules)

cardexpansions = Forward().setParseAction(act.cardexpansions)

card = Forward().setParseAction(act.card)