from pyparsing import *

from ...constants.articles.deff import *
from ...constants.prepositions.deff import UPTO
from ...constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM

from decl import *

change << Optional(PLUS|MINUS) + amount
amount << ((NUM + change) | NUM | (XVAR + change) | XVAR | FULLNUM)

uptoamount << UPTO + amount
an << AN
another << ANOTHER
alll << ALL

quantity << (an | another | alll | amount | uptoamount)

target << TARGET
quantitytarget << quantity + TARGET
this << THIS
that << THAT
other << OTHER
each << EACH
the << THE

# beware of ordering, it's match-first
det << (quantitytarget | quantity | target | this | that | other | each | the)