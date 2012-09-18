from pyparsing import *
from basic import *
from pt_h import * 

ptchange << Group((PLUS | MINUS) + number)
ptquantity << (ASTERISK | number | (ASTERISK + ptchange))
ptmod << Group(ptchange + Suppress(SLASH) + ptchange)

XVAR << Keyword("X")

loyalty << number
loyaltycost << Group(LBRACKET + Optional(PLUS|MINUS) + (number|XVAR) + RBRACKET)

cardpt << (Group(ptquantity + Suppress(SLASH) + ptquantity)|Group(loyalty))