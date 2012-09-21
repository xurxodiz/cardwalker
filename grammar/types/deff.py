from pyparsing import *

from ..basic.constants.deff import *
from ..basic.functions.deff import *

from decl import *

supertype << load_from_file("oracle/ref/supertypes.txt")

type_ << load_from_file("oracle/ref/types.txt")

basic_land_type << load_from_file("oracle/ref/basic_land_types.txt")

other_land_type << load_from_file("oracle/ref/other_land_types.txt")

land_type << (basic_land_type | other_land_type)

creature_type << load_from_file("oracle/ref/creature_types.txt")

tribal_type << creature_type

artifact_type << load_from_file("oracle/ref/artifact_types.txt")

planeswalker_type << load_from_file("oracle/ref/planeswalker_types.txt")

enchantment_type << load_from_file("oracle/ref/enchantment_types.txt")

spell_type << load_from_file("oracle/ref/spell_types.txt")

subtype << (spell_type | enchantment_type | planeswalker_type | artifact_type | creature_type | land_type)

nontype << NON + (supertype | subtype | type_)

supertypes << OneOrMore(supertype)

types << OneOrMore(type_)

subtypes << OneOrMore(subtype)

cardtypeline << (
	Optional(supertypes)
	+ types
	+ Optional(Suppress(DASH) + subtypes)
) + EOL