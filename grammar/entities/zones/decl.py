from pyparsing import *

import act

detzone = Forward().setParseAction(act.detzone)
thebattlefield = Forward().setParseAction(act.thebattlefield)
thetopbottomoflibrary = Forward().setParseAction(act.thetopbottomoflibrary)

zone = Forward().setParseAction(act.zone)

inzone = Forward().setParseAction(act.inzone)
ofzone = Forward().setParseAction(act.ofzone)
fromzone = Forward().setParseAction(act.fromzone)

where = Forward()