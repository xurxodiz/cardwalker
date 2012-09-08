from pyparsing import *
from basic import *

ptchange = (PLUS | MINUS) + number
ptquantity = ASTERISK | number | (ASTERISK + ptchange)
ptmod = ptchange + Suppress(SLASH) + ptchange

cardpt = Group(ptquantity + Suppress(SLASH) + ptquantity)