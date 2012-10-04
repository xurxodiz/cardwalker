from pyparsing import *

from ...functions.deff import oneOfNamed

from decl import *

MAY << CaselessLiteral("may")

BE << oneOfNamed("is are be")
HAVE << oneOfNamed("has have")
GET << oneOfNamed("get gets")
CANT << CaselessLiteral("can't")
MUST << CaselessLiteral("must")
WOULD << CaselessLiteral("would")

DESTROY << oneOfNamed("destroy destroys destroyed")
EXILE << oneOfNamed("exile exiles exiled")
GAIN << oneOfNamed("gain gains gained")
LOSE << oneOfNamed("lose loses lost")
TAP << oneOfNamed("tap taps tapped")
UNTAP << oneOfNamed("untap untaps untapped")
DISCARD << oneOfNamed("discard discards discarded")
SACRIFICE << oneOfNamed("sacrifice sacrifices sacrificed")
DRAW << oneOfNamed("draw draws drawn")
DEAL << oneOfNamed("deal deals dealt")
PAY << oneOfNamed("pay pays paid")
PUT << oneOfNamed("put puts")
ATTACK << oneOfNamed("attack attacks attacking attacked")
BLOCK << oneOfNamed("block blocks blocking blocked")
BECOME << oneOfNamed("become becomes")
REDUCE << oneOfNamed("reduce reduced reduces")
RETURN << oneOfNamed("return returned returns")
ENTER << oneOfNamed("enter enters entered")
LEAVE << oneOfNamed("leave leaves left")
DIE << oneOfNamed("die dies died")
PREVENT << oneOfNamed("prevent prevents prevented")
ADD << oneOfNamed("add adds added")
REGENERATE << oneOfNamed("regenerate regenerates regenerated")
CONTROL << oneOfNamed("control controls controlled")
COUNTERSPELL << oneOfNamed("counter counters")

# keywords:

EQUIP << oneOfNamed ("equip equipped")
FORTIFY << oneOfNamed ("fortify fortified")
HAUNT << oneOfNamed ("haunt haunted")
ENCHANT << oneOfNamed ("enchant enchanted")