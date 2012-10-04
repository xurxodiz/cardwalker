from pyparsing import *

from ..constants.types.deff import *
from ..constants.modifiers.deff import NON
from ..constants.punctuation.deff import DASH, EOL, APOS

from decl import *

cardname << (CARDNAME)

supertype << SUPERTYPE
type_ << TYPE_
basic_land_type << BASICLANDTYPE
other_land_type << OTHERLANDTYPE
creature_type << CREATURETYPE
artifact_type << ARTIFACTTYPE
planeswalker_type << PLANESWALKERTYPE
enchantment_type << ENCHANTMENTTYPE
spell_type << SPELLTYPE

land_type << (basic_land_type | other_land_type)
tribal_type << creature_type
subtype << (spell_type | enchantment_type | planeswalker_type | artifact_type | creature_type | land_type)

nontype << NON + (supertype | subtype | type_)

cardsupertypes << OneOrMore(supertype)
cardtypes << OneOrMore(type_)
cardsubtypes << OneOrMore(subtype)

cardtypeline << (
	Optional(cardsupertypes)
	+ cardtypes
	+ Optional(Suppress(DASH) + cardsubtypes)
)