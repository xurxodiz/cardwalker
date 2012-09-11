from pyparsing import *
from basic import *

THIS = CaselessLiteral("this")
THAT = CaselessLiteral("that")

BE = or_cs(["is", "are"])
HAVE = or_cs(["has", "have"])
GET = or_cs(["get", "gets"])
FROM = Suppress("from")
AN = or_cs(["a", "an"])
THE = CaselessLiteral("the")
OTHER = CaselessLiteral("other")
ANOTHER = CaselessLiteral("another")

WHEN = or_cl (["when", "whenever"])
TARGET = CaselessLiteral("target")
MAY = CaselessLiteral("may")
TO = CaselessLiteral("to")
UPTO = CaselessLiteral("up") + TO

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
DEAL = or_cl(["deal", "deals"])
DAMAGE = CaselessLiteral("damage")
PAY = or_cl(["pay", "pays"])

SPELL = or_cl(["spell", "spells"])
PERMANENT = or_cl(["permanent", "permanents"])
CARD = or_cl(["card", "cards"])
ABILITY = or_cl(["ability", "abilities"])

CONTROL = or_cl (["control", "controls"])
IT = CaselessLiteral("it")
IN = CaselessLiteral("in")
HIS = CaselessLiteral("his or her")
ALL = CaselessLiteral("all")
EACH = CaselessLiteral("each")

YOU = CaselessLiteral("you")
PLAYER = or_cl(["player", "players"])
OPPONENT = or_cl(["opponent", "opponents"])

YOUR = CaselessLiteral("your")
POSS = or_cl(["' ", "'s"])

HAND = or_cl(["hand", "hands"])
GRAVEYARD = or_cl(["graveyard", "graveyards"])
LIBRARY = or_cl(["library", "libraries"])
EXILE = CaselessLiteral("exile")
BATTLEFIELD = CaselessLiteral("battlefield")

ATRANDOM = CaselessLiteral("at random")