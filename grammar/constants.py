from pyparsing import *
from basic import *

THIS = CaselessLiteral("this")
THAT = CaselessLiteral("that")

BE = or_cs(["is", "are"])
HAVE = or_cs(["has", "have"])
GET = or_cs(["get", "gets"])
FROM = Suppress("from")
AN = or_cs(["a", "an"])

WHEN = or_cl (["when", "whenever"])
TARGET = CaselessLiteral("target")
MAY = CaselessLiteral("may")
UPTO = CaselessLiteral("up to")

DESTROY = or_cl(["destroy", "destroys"])
EXILE = or_cl(["exile", "exiles"])
GAIN = or_cl(["gain", "gains"])
LIFE = CaselessLiteral("life")
LOSE = or_cl(["lose", "loses"])
TAP = or_cl(["tap", "taps"])
UNTAP = or_cl(["untap", "untaps"])
DISCARD = or_cl(["discard", "discards"])
SACRIFICE = or_cl(["sacrifice", "sacrifices"])
DRAW = or_cl(["draw", "draws"])

SPELL = or_cl(["spell", "spells"])
PERMANENT = or_cl(["permanent", "permanents"])
CARD = or_cl(["card", "cards"])
ABILITY = or_cl(["ability", "abilities"])

CONTROL = or_cl (["control", "controls"])
IT = CaselessLiteral("it")