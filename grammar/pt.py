from pyparsing import *
from basic import *

ptchange = Group((PLUS | MINUS) + number)
ptquantity = ASTERISK | number | (ASTERISK + ptchange)
ptmod = Group(ptchange + Suppress(SLASH) + ptchange)

cardpt = Group(ptquantity + Suppress(SLASH) + ptquantity)