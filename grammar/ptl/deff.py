from pyparsing import *

from ..constants.punctuation.deff import SLASH, LBRACKET, RBRACKET, EOL
from ..constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM
from ..entities.deff import change, amount

from decl import * 

ptmod << change + SLASH + change
loyaltymod << (LBRACKET + change + RBRACKET)

loyaltystart << amount
ptstart << (amount + SLASH + amount)

cardptl << (ptstart|loyaltystart) + EOL