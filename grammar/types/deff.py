from pyparsing import *

from ..basic.constants.deff import *
from ..basic.functions.deff import *

from decl import *

basic_land_type << load_from_file("oracle/ref/basic_land_type.txt")

other_land_type << load_from_file("oracle/ref/other_land_type.txt")

creature_type << load_from_file("oracle/ref/creature_type.txt")

artifact_type << load_from_file("oracle/ref/artifact_type.txt")

planeswalker_type << load_from_file("oracle/ref/planeswalker_type.txt")

enchantment_type << load_from_file("oracle/ref/enchantment_type.txt")

spell_type << load_from_file("oracle/ref/spell_type.txt")

supertype << load_from_file("oracle/ref/supertype.txt")

land_type << (basic_land_type | other_land_type)

tribal_type << creature_type

subtype << (spell_type | enchantment_type | planeswalker_type | artifact_type | creature_type | land_type)

creature << oneOf("Creature Creatures", caseless=True)

token << oneOf("Token Tokens", caseless=True)

tribal << oneOf("Tribal Tribals", caseless=True)

instant << oneOf("Instant Instants", caseless=True)

sorcery << oneOf("Sorcery Sorceries", caseless=True)

land << oneOf("Land Lands", caseless=True)

artifact << oneOf("Artifact Artifacts", caseless=True)

enchantment << oneOf("Enchantment Enchantments", caseless=True)

planeswalker << oneOf("Planeswalker Planeswalkers", caseless=True)

type_ << (token | creature | tribal | instant | sorcery
				| land | artifact | enchantment | planeswalker)

nontype << NON + (supertype | subtype | type_)

supertypes << OneOrMore(supertype)

types_ << OneOrMore(type_)

subtypes << OneOrMore(subtype)

cardtypeline << (
	Optional(supertypes)
	+ types_
	+ Optional(Suppress(DASH) + subtypes)
) + EOL