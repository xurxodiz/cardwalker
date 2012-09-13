from pyparsing import *
from basic import *

ptchange = Group((PLUS | MINUS) + number)
ptquantity = ASTERISK | number | (ASTERISK + ptchange)
ptmod = Group(ptchange + Suppress(SLASH) + ptchange)

XCHANGE = Literal("X")

loyalty = number
loyaltycost = Group(LBRACKET + Optional(PLUS|MINUS) + (number|XCHANGE) + RBRACKET)

cardpt = Group(ptquantity + Suppress(SLASH) + ptquantity)|Group(loyalty)