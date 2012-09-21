from pyparsing import *

import act

colorname = Forward().setParseAction(act.colorname)
noncolorname = Forward().setParseAction(act.noncolorname)
abschar = Forward().setParseAction(act.abschar)
color = Forward()

manasymbol = Forward().setParseAction(act.manasymbol)
tapsymbol = Forward().setParseAction(act.tapsymbol)
untapsymbol = Forward().setParseAction(act.untapsymbol)
snowsymbol = Forward().setParseAction(act.snowsymbol)

phyletter = Forward()
physymbol = Forward().setParseAction(act.physymbol)
chybsymbol = Forward().setParseAction(act.chybsymbol)
hybsymbol = Forward().setParseAction(act.hybsymbol)

numcost = Forward().setParseAction(act.numcost)
xcost = Forward().setParseAction(act.xcost)

singlecost = Forward()
manapayment = Forward().setParseAction(act.manapayment)

cardcost = Forward().setParseAction(act.cardcost)