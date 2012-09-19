from pyparsing import *

import act

change = Forward().setParseAction(act.change)
amount = Forward().setParseAction(act.amount)

loyaltymod = Forward().setParseAction(act.loyaltymod)
ptmod = Forward().setParseAction(act.ptmod)


loyaltystart = Forward().setParseAction(act.loyaltystart)
ptstart = Forward().setParseAction(act.ptstart)

cardptl = Forward()