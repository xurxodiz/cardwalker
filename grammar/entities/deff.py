from pyparsing import *

from ..constants.prepositions.deff import UPTO, OF, IN, FROM
from ..constants.articles.deff import *
from ..constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM
from ..constants.people.deff import *
from ..constants.verbs.deff import MAY, HAVE, CONTROL, TAP, UNTAP, ENCHANT, EQUIP, EXILE, SACRIFICE, HAUNT
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

det << (globaldet|peopleposs)

# usting just 'det' ends in infinite left recursion
# thus the differentiation above
detpeople << globaldet + (PLAYER | OPPONENT | CONTROLLER | OWNER)

people << delimitedListAnd(YOU|detpeople)

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
consadjectives << OneOrMore(adjective)

adjectives << (consadjectives | andadjectives | oradjectives)

noun << (subtype | type_ | concept)

andnoun << delimitedListAnd(noun)
ornoun << delimitedListOr(noun)
consnoun << OneOrMore(noun)

baseobject_ << OneOrMore(consnoun | andnoun | ornoun)

object_ << Optional(det) + Optional(adjectives) + baseobject_
orobjects << delimitedListOr(object_)
andobjects << delimitedListAnd(object_)
consobjects << OneOrMore(object_ )

it << IT
they << THEY

objects << (
	(andobjects | orobjects | consdetobjects | cardname) + Optional(where)
)

mayer << people + MAY + Optional(HAVE + (people|objects))
subject << (it|they|resource|mayer|people|objects)