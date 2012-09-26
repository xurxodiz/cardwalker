from pyparsing import *

from decl import *

MAY << CaselessLiteral("may")

BE << oneOfNamed("is are", caseless=True)
HAVE << oneOfNamed("has have", caseless=True)
GET << oneOfNamed("get gets", caseless=True)
CANT << CaselessLiteral("can't")
MUST << CaselessLiteral("must")

DESTROY << oneOfNamed("destroy destroys destroyed", caseless=True)
EXILE << oneOfNamed("exile exiles exiled", caseless=True)
GAIN << oneOfNamed("gain gains gained", caseless=True)
LOSE << oneOfNamed("lose loses lost", caseless=True)
TAP << oneOfNamed("tap taps tapped", caseless=True)
UNTAP << oneOfNamed("untap untaps untapped", caseless=True)
DISCARD << oneOfNamed("discard discards discarded", caseless=True)
SACRIFICE << oneOfNamed("sacrifice sacrifices sacrificed", caseless=True)
DRAW << oneOfNamed("draw draws drawn", caseless=True)
DEAL << oneOfNamed("deal deals dealt", caseless=True)
PAY << oneOfNamed("pay pays paid", caseless=True)
PUT << oneOfNamed("put puts", caseless=True)
ATTACK << oneOfNamed("attack attacks attacking attacked", caseless=True)
BLOCK << oneOfNamed("block blocks blocking blocked", caseless=True)
BECOME << oneOfNamed("become becomes", caseless=True)
REDUCE << oneOfNamed("reduce reduced reduces", caseless=True)
RETURN << oneOfNamed("return returned returns", caseless=True)
ENTER << oneOfNamed("enter enters entered", caseless=True)
LEAVE << oneOfNamed("leave leaves left", caseless=True)
DIE << oneOfNamed("die dies died", caseless=True)
PREVENT << oneOfNamed("prevent prevents prevented", caseless=True)
ADD << oneOfNamed("add adds added", caseless=True)
REGENERATE << oneOfNamed("regenerate regenerates regenerated", caseless=True)
CONTROL << oneOfNamed("control controls controlled", caseless=True)
COUNTERSPELL << oneOfNamed("counter counters", caseless=True)

# keywords:

EQUIP << oneOfNamedNamed ("equip equipped")
FORTIFY << oneOfNamedNamed ("fortify fortified")
HAUNT << oneOfNamedNamed ("haunt haunted")
ENCHANT << oneOfNamedNamed ("enchant enchanted")