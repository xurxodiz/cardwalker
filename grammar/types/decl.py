from pyparsing import *

basic_land_type = Forward()

other_land_type = Forward()

creature_type = Forward()

artifact_type = Forward()

planeswalker_type = Forward()

enchantment_type = Forward()

spell_type = Forward()

supertype = Forward()

land_type = Forward()

tribal_type = Forward()

subtype = Forward()

creature = Forward()

token = Forward()

tribal = Forward()

instant = Forward()

sorcery = Forward()

land = Forward()

artifact = Forward()

enchantment = Forward()

planeswalker = Forward()

type_ = Forward()

nontype = Forward()

supertypes = Forward()

types_ = Forward()

subtypes = Forward()

cardtypeline = Forward()