from pyparsing import *

from ..constants.prepositions.deff import UPTO, OF, IN, FROM
from ..constants.articles.deff import *
from ..constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM
from ..constants.people.deff import *
from ..constants.verbs.deff import *
from ..constants.zones.deff import GRAVEYARD, BATTLEFIELD, HAND, LIBRARY, TOP, BOTTOM
from ..constants.concepts.deff import concept, IT, THEY
from ..constants.resources.deff import LIFE, TOTAL, SIZE
from ..mana.deff import color
from ..types.deff import cardname, nontype, supertype, subtype, type_

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
its << ITS
the << THE

globaldet << (quantitytarget | quantity | target | this | that | other | each | its | the)

det << (peopleposs|globaldet)

# usting just 'det' ends in infinite left recursion
# because of peoplepos
# thus the hack with globaldet/YOUR
detpeople << (globaldet|YOUR) + (PLAYER | OPPONENT | CONTROLLER | OWNER)

people << delimitedListAnd(detpeople|YOU)

your << YOUR
their << THEIR
his << HIS
peoploss << people + POSS

peopleposs << (your|their|his|peoploss)

detzone << det + (GRAVEYARD|HAND|LIBRARY)
thebattlefield << THE + BATTLEFIELD
thetopbottomoflibrary << THE + (TOP|BOTTOM) + OF + peopleposs + LIBRARY

zone << (detzone|thebattlefield|thetopbottomoflibrary)

peoplecontrol << people + CONTROL
inzone << IN + zone
ofzone << OF + zone
fromzone << FROM + zone

where << (peoplecontrol|inzone|ofzone|fromzone)

lifetotal << peopleposs + LIFE + TOTAL
handsize << peopleposs + HAND + SIZE

resource << (lifetotal|handsize)

topnum << (TOP|BOTTOM) + (NUM|FULLNUM)

attacking << ATTACK
blocking << BLOCK
tapped << TAP
untapped << UNTAP
enchanted << ENCHANT
equipped << EQUIP
exiled << EXILE
sacrificed << SACRIFICE
haunted << HAUNT

adjective << ( \
	color
	| nontype
	| supertype
	| topnum
	| attacking
	| blocking
	| tapped
	| untapped
	| enchanted
	| equipped
	| exiled
	| sacrificed
	| haunted
)

andadjectives << delimitedListAnd(adjective)
oradjectives << delimitedListOr(adjective)

adjectives << OneOrMore(andadjectives ^ oradjectives)

noun << (subtype | type_ | concept)

andnoun << delimitedListAnd(noun)
ornoun << delimitedListOr(noun)

baseobject_ << OneOrMore(andnoun ^ ornoun)

object_ << Optional(det) + Optional(adjectives) + baseobject_
orobjects << delimitedListOr(object_)
andobjects << delimitedListAnd(object_)

it << IT
they << THEY

objects << OneOrMore(
	(andobjects ^ orobjects
	| cardname
	| it
	| they
	) + Optional(where)
)

mayer << people + MAY + Optional(HAVE + (people|objects))
subject << (it|they|resource|mayer|people|objects)