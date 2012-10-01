from pyparsing import *

import act

basic_keyword = Forward().setParseAction(act.basic_keyword)
number_keyword = Forward().setParseAction(act.number_keyword)
costed_keyword = Forward().setParseAction(act.costed_keyword)

haunt = Forward().setParseAction(act.haunt)
equip = Forward().setParseAction(act.equip)
fortify = Forward().setParseAction(act.fortify)
enchant = Forward().setParseAction(act.enchant)

cycling = Forward().setParseAction(act.cycling)
landwalk = Forward().setParseAction(act.landwalk)
protection = Forward().setParseAction(act.protection)

keywords = Forward().setParseAction(act.keywords)