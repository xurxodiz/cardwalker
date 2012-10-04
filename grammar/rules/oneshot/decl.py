from pyparsing import *

import act

nextquantity = Forward().setParseAction(act.nextquantity)

damage = Forward().setParseAction(act.damage)
combatdamage = Forward().setParseAction(act.combatdamage)
noncombatdamage = Forward().setParseAction(act.noncombatdamage)

thedamage = Forward()

thisturn = Forward().setParseAction(act.thisturn)

where = Forward().setParseAction(act.where)
equal = Forward().setParseAction(act.equal)
for_ = Forward().setParseAction(act.for_)

undercontrol = Forward().setParseAction(act.undercontrol)

destroy = Forward().setParseAction(act.destroy)
cantregenerate = Forward().setParseAction(act.cantregenerate)
exile = Forward().setParseAction(act.exile)
gainlife = Forward().setParseAction(act.gainlife)
tap = Forward().setParseAction(act.tap)
untap = Forward().setParseAction(act.untap)
draw = Forward().setParseAction(act.draw)
discard = Forward().setParseAction(act.discard)
loselife = Forward().setParseAction(act.loselife)
dealquantitydamage = Forward().setParseAction(act.dealquantitydamage)
dealdamage = Forward().setParseAction(act.dealdamage)
sacrifice = Forward().setParseAction(act.sacrifice)
regenerate = Forward().setParseAction(act.regenerate)
putcounter = Forward().setParseAction(act.putcounter)

tokens = Forward().setParseAction(act.tokens)
puttoken = Forward().setParseAction(act.puttoken)

return_ = Forward().setParseAction(act.return_)
become = Forward().setParseAction(act.become)
bereduced = Forward().setParseAction(act.bereduced)
paylife = Forward().setParseAction(act.paylife)
prevention = Forward().setParseAction(act.prevention)
addmana = Forward().setParseAction(act.addmana)
counterspell = Forward().setParseAction(act.counterspell)

quantifier = Forward()

effect = Forward().setParseAction(act.effect)

oneshot = Forward().setParseAction(act.oneshot)