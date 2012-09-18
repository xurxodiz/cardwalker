from pyparsing import *

from def import *
from ..basic.constants import *
from ..basic.functions import * 

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

creature << oneOf("creature creatures", caseless=True)

token << oneOf("token tokens", caseless=True)

tribal << oneOf("tribal tribals", caseless=True)

instant << oneOf("instant instants", caseless=True)

sorcery << oneOf("sorcery sorceries", caseless=True)

land << oneOf("land lands", caseless=True)

artifact << oneOf("artifact artifacts", caseless=True)

enchantment << oneOf("enchantment enchantments", caseless=True)

planeswalker << oneOf("planeswalker planeswalkers", caseless=True)

type_ << (token | creature | tribal | instant | sorcery
				| land | artifact | enchantment | planeswalker)

nontype << Group(NON + (supertype | subtype | type_))

supertypes << OneOrMore(supertype)

types_ << OneOrMore(type_)

subtypes << OneOrMore(subtype)

cardtypeline << Group(
	Optional(Group(supertypes))
	+ Group(types_)
	+ Optional(Group(Suppress(DASH) + subtypes))
)