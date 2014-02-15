from pyparsing import *

from decl import *

from ..keywords.deff import keywords
from ...constants.articles.deff import EACH
from ...constants.connectors.deff import IF
from ...constants.modifiers.deff import ABLE
from ...constants.prepositions.deff import UNTIL, OF
from ...constants.verbs.deff import HAVE, GET, BE, GAIN, CONTROL, CANT, MUST, ATTACK, BLOCK
from ...constants.timing.deff import TURN, UPKEEP, DRAWSTEP, PRECOMBAT, COMBAT, POSCOMBAT, END
from ...entities.subjects.deff import subjects, objects
from ...functions.deff import delimitedListAnd
from ...ptl.deff import ptmod

#thisturn << THIS + TURN
until << UNTIL + END + OF + TURN
# add as-long-as clause
# remember it can go before or after the effect

havekeywords << HAVE + delimitedListAnd(keywords)
getptmod << GET + ptmod
gaincontrol << GAIN + CONTROL + OF + objects

#attack << ATTACK
#block << BLOCK

# one of the cases where "or" means "both" and not "option", beware!
#cantattackorblock << CANT + delimitedListOr(attack|block) 

# add "can't be blocked [by X]"

#mustattack << MUST + ATTACK + EACH + TURN
#mustbeblocked << MUST + BE + BLOCK

property_ << (
	havekeywords
	| getptmod
	| gaincontrol
	#| cantattackorblock
	#| mustattack
)

properties << delimitedListAnd(property_)

continuous << subjects + properties + Optional(until)#+ ZeroOrMore(until|thisturn|ifable)