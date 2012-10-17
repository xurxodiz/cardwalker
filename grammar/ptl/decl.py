from pyparsing import *

import act

loyaltymod = Forward().setParseAction(act.loyaltymod)
ptmod = Forward().setParseAction(act.ptmod)

loyaltystart = Forward().setParseAction(act.loyaltystart)
ptstart = Forward().setParseAction(act.ptstart)