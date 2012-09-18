from pyparsing import *
from definitions import *
from basic import *
from types import *
from mana import *
from rules import *

PROTECTION << CaselessLiteral("Protection")
WALK << CaselessLiteral("Walk")
ENCHANT << CaselessLiteral("Enchant")

landwalk << (
		basic_land_type + WALK
)

basic_keyword << or_cl ([ \
				"Flying",
				"Deathtouch",
				"Trample",
				"Haste",
				"Flash",
				"Vigilance",
				"Intimidate",
				"Exalted",
				"Lifelink", 
				"Hexproof",
				"Flanking",
				"Shadow",
				"Shroud",
				"Persist",
				"Living weapon",
				"Battle cry",
				"Infect",
				"Wither",
				"Storm",
				"Convoke",
				"Radiance",
				"Haunt",
				"Undying",
				"Double strike",
				"First strike",
				"Unleash",
				"Epic",
				"Sunburst",
				"Cascade",
				"Changeling",
				"Conspire",
				"Convoke",
				"Delve",
				"Gravestorm",
				"Hideaway",
				"Horsemanship",
				"Phasing",
				"Provoke",
				"Rebound",
				"Retrace",
				"Soulbond",
				"Split second",
				"Totem arbor",
				"Fear",
				"Defender"
])

number_keyword << or_cl([ \
					"Rampage",
					"Soulshifting",
					"Bushido",
					"Absorb",
					"Annihilator",
					"Amplify",
					"Bloodthirst",
					"Devour",
					"Dredge",
					"Fading",
					"Vanishing",
					"Fateseal",
					"Scry",
					"Graft",
					"Modular",
					"Poisonous",
					"Reinforce",
					"Ripple",
])

EQUIP << or_cl(["equip", "equipped"])
FORTIFY << or_cl(["fortify", "fortified"])
HAUNT << or_cl(["haunt", "haunted"])
ENCHANT << or_cl(["enchant", "enchanted"])


CYCLING << CaselessLiteral("Cycling")
cycling << Group(Optional(basic_land_type|subtype) + CYCLING)


costed_keyword << (or_cl([ \
					"Morph",
					"Kicker",
					"Multickicker",
					"Replicate",
					"Madness",
					"Unearth",
					"Flashback",
					"Miracle",
					"Overload",
					"Scavenge",
					"Madness",
					"Aura swap",
					"Buyback",
					"Echo",
					"Entwine",
					"Evoke",
					"Suspend",
					"Level up",
					"Ninjutsu",
					"Prowl",
					"Recover",
					"Replicate",
					"Transfigure",
					"Transmute",
					])
				| EQUIP
				| FORTIFY
				| cycling
)

protection << Group(PROTECTION + delimitedListAnd(FROM + color))

ability_keyword << (or_cl([ \
				"Cumulative upkeep",
				"Domain",
				"Channel",
				"Forecast",
				"Chroma",
				"Fateful hour",
				"Grandeur",
				"Hellbent",
				"Imprint",
				"Join forces",
				"Kinship",
				"Landfall",
				"Metalcraft",
				"Morbid",
				"Sweep",
				"Threshold",


]))

enchant << ENCHANT + objects

keywords << delimitedListAnd( \
		basic_keyword
		| number_keyword + (XVAR|number|(DASH + cardrules))
		| costed_keyword + (manapayment|(DASH + oneshot)) 
		| ability_keyword + DASH + cardrules
		| enchant
		| protection
		| landwalk
		| enchant
)

INDESTRUCTIBLE << CaselessLiteral("indestructible")
UNBLOCKABLE << CaselessLiteral("unblockable")