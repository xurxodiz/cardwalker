from pyparsing import *

from decl import *

from ..keywords.deff import keywords
from ...constants.prepositions.deff import UNTIL, OF
from ...constants.verbs.deff import HAVE, GET, BE, GAIN, CONTROL, CANT, MUST, ATTACK, BLOCK
from ...constants.timing.deff import TURN, UPKEEP, DRAWSTEP, PRECOMBAT, COMBAT, POSCOMBAT, END
from ...constants.keywords.deff import INDESTRUCTIBLE, UNBLOCKABLE
from ...entities.objects.deff import objects
from ...entities.subjects.deff import subject
from ...functions.deff import delimitedListAnd
from ...ptl.deff import ptmod

turn << TURN
upkeep << UPKEEP
drawstep << DRAWSTEP
precombat << PRECOMBAT
combat << COMBAT
poscombat << POSCOMBAT

step << (turn|upkeep|drawstep|precombat|combat|poscombat)

until << UNTIL + END + OF + TURN

havekeywords << HAVE + delimitedListAnd(keywords)
getptmod << GET + ptmod
beindestructible << BE + INDESTRUCTIBLE
beunblockable << BE + UNBLOCKABLE
gaincontrol << GAIN + CONTROL + OF + objects
cantblock << CANT + BLOCK
mustattack << MUST + ATTACK 

#quotedtriggered << (QUOTE + triggered + QUOTE)
#quotedactivated << (QUOTE + activated + QUOTE)
#abilities << delimitedListAnd(keywords|ptmod|quotedtriggered|quotedactivated)
#gainabilities << GAIN + abilities

property_ << (
	havekeywords
	| getptmod
	| beindestructible
	| beunblockable
	#| gainabilities
	| gaincontrol
	| cantblock
	| mustattack
)

properties << delimitedListAnd(property_)

continuous << subject + properties + Optional(until)