from pyparsing import *

import act

PROTECTION = Forward()
WALK = Forward()
INDESTRUCTIBLE = Forward()
UNBLOCKABLE = Forward()

CYCLING = Forward()
cycling = Forward().setParseAction(act.cycling)

protection = Forward().setParseAction(act.protection)
enchant = Forward()
landwalk = Forward().setParseAction(act.landwalk)

ability_keyword = Forward()
basic_keyword = Forward().setParseAction(act.basic_keyword)
number_keyword = Forward().setParseAction(act.number_keyword)
costed_keyword = Forward().setParseAction(act.costed_keyword)
keywords = Forward()