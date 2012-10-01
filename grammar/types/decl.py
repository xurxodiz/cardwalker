from pyparsing import *

import act

cardname = Forward().setParseAction(act.cardname)

supertype = Forward().setParseAction(act.supertype)
type_ = Forward().setParseAction(act.type_)

basic_land_type = Forward()
other_land_type = Forward()
land_type = Forward()
creature_type = Forward()
tribal_type = Forward()
artifact_type = Forward()
planeswalker_type = Forward()
enchantment_type = Forward()
spell_type = Forward()
subtype = Forward().setParseAction(act.subtype)

nontype = Forward().setParseAction(act.nontype)

cardsupertypes = Forward().setParseAction(act.cardsupertypes)
cardtypes = Forward().setParseAction(act.cardtypes)
cardsubtypes = Forward().setParseAction(act.cardsubtypes)

cardtypeline = Forward().setParseAction(act.cardtypeline)
