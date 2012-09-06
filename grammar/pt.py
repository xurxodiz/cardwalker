from pyparsing import *
from basic import *

ptchange = (plus | minus) + number
ptquantity = asterisk | number | (asterisk + ptchange)
ptmod = ptchange + Suppress(slash) + ptchange

cardpt = Group(ptquantity + Suppress(slash) + ptquantity)