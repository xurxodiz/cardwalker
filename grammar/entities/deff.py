from pyparsing import *

from ..constants.prepositions.deff import UPTO, OF, IN, FROM
from ..constants.articles.deff import *
from ..constants.math.deff import PLUS, MINUS, NUM, XVAR, FULLNUM
from ..constants.people.deff import *
from ..constants.verbs.deff import MAY, HAVE, CONTROL, TAP, UNTAP, ENCHANT, EQUIP, EXILE, SACRIFICE, HAUNT
from ..constants.zones.deff import GRAVEYARD, BATTLEFIELD, HAND, LIBRARY, TOP, BOTTOM
from ..constants.concepts.deff import concept
from ..constants.resources.deff import LIFE, TOTAL, SIZE
from ..mana.deff import color
from ..types.deff import cardname, nontype, supertype, subtype, type_, subtypes, types


from decl import *

change << Optional(PLUS|MINUS) + amount
amount << ((NUM + change) | NUM | (XVAR + change) | XVAR | FULLNUM)

uptoamount << UPTO + amount
an << AN
another << ANOTHER
alll << ALL

quantity << (amount|uptoamount|an|another|alll)

target << TARGET
quantitytarget << quantity + TARGET
this << THIS
that << THAT
other << OTHER
each << EACH
its << ITS
the << THE

det << (target|quantitytarget|quantity|peopleposs|this|that|other|each|its|the)

people << delimitedListAnd(
	Optional(det)
	+ (YOU | PLAYER | OPPONENT | CONTROLLER | OWNER)
)

your << YOUR
their << THEIR
his << HIS
peoploss << people + POSS

peopleposs << (your|their|his|peoploss)

detzone << det + (GRAVEYARD|HAND|LIBRARY)
thebattlefield << THE + BATTLEFIELD
thetopoflibrary << THE + TOP + OF + peopleposs + LIBRARY

zone << (detzone|thebattlefield|thetopoflibrary)

peoplecontrol << people + CONTROL
inzone << IN + zone
ofzone << OF + zone
fromzone << FROM + zone

where << (peoplecontrol|inzone|ofzone|fromzone)

lifetotal << peopleposs + LIFE + TOTAL
handsize << peopleposs + HAND + SIZE

resource << (lifetotal|handsize)

adjective << ( \
	color
	| nontype
	| supertype
	| (TOP|BOTTOM) + (NUM|FULLNUM)
	# coming next: participles
	| TAP
	| UNTAP
	| ENCHANT
	| EQUIP
	| EXILE
	| SACRIFICE
	| HAUNT
)

andadjectives << delimitedListAnd(adjective)
oradjectives << delimitedListOr(adjective)
consadjectives << OneOrMore(adjective)

adjectives << (andadjectives|oradjectives|consadjectives)

andsubtypes << delimitedListAnd(subtype)
orsubtypes << delimitedListOr(subtype)

thesubtypes << (andsubtypes|orsubtypes|subtypes)

andtypes << delimitedListAnd(type_)
ortypes << delimitedListOr(type_)

thetypes << (andtypes|ortypes|types)

andconcepts << delimitedListAnd(concept)
orconcepts << delimitedListOr(concept)
consconcepts << OneOrMore(concept)

theconcepts << (andconcepts|orconcepts|consconcepts)

baseobject_ << (thesubtypes|thetypes|theconcepts)

object_ << Optional(adjectives) + baseobject_ + Optional(where)

objects << (
	delimitedListAnd(
		Optional(det)
		+ delimitedListOr(object_)
	)
	| cardname
)

mayer << people + Optional(MAY + Optional(HAVE + (people|objects)))
subject << (resource|mayer|people|objects)