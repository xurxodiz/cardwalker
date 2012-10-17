from pyparsing import *

import act

change = Forward().setParseAction(act.change)
amount = Forward().setParseAction(act.amount)

uptoamount = Forward().setParseAction(act.uptoamount)
an = Forward().setParseAction(act.an)
another = Forward().setParseAction(act.another)
alll = Forward().setParseAction(act.alll)

quantity = Forward()

target = Forward().setParseAction(act.target)
quantitytarget = Forward().setParseAction(act.quantitytarget)
this = Forward().setParseAction(act.this)
that = Forward().setParseAction(act.that)
other = Forward().setParseAction(act.other)
each = Forward().setParseAction(act.each)
the = Forward().setParseAction(act.the)

det = Forward().setParseAction(act.det)

globaldet = Forward()