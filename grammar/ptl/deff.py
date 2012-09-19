from pyparsing import *
from ..basic.constants.deff import *

from decl import * 

change << Optional(PLUS|MINUS) + amount
amount << ((NUM + change) | NUM | (XVAR + change) | XVAR)

ptmod << change + SLASH + change
loyaltymod << (LBRACKET + change + RBRACKET)

loyaltystart << amount
ptstart << (amount + SLASH + amount)

cardptl << (ptstart|loyaltystart)