from pyparsing import *
from basic import *

a_spell = or_cl(["spell", "spells"])
a_permanent = or_cl(["permanent", "permanents"])
a_card = or_cl(["card", "cards"])
an_ability = or_cl(["ability", "abilities"])

a_concept = a_spell | a_permanent | a_card | an_ability

basic_land_type = or_cl (["Plains", "Forest", "Mountain", "Swamp", "Island"])

other_land_type = or_cl (["Desert", "Lair", "Locus", "Mine", "Power-Plant", "Tower", "Urza's"])

land_type = basic_land_type | other_land_type

creature_type = or_cl \
	(["Advisor", "Ally", "Angel", "Anteater", "Antelope", "Ape", "Archer",
	"Archon", "Artificer", "Assassin", "Assembly-Worker", "Atog",
	"Aurochs", "Avatar", "Badger", "Barbarian", "Basilisk", "Bat",
	"Bear", "Beast", "Beeble", "Berserker", "Bird", "Blinkmoth", "Boar",
	"Bringer", "Brushwagg", "Camarid", "Camel", "Caribou", "Carrier",
	"Cat", "Centaur", "Cephalid", "Chimera", "Citizen", "Cleric",
	"Cockatrice", "Construct", "Coward", "Crab", "Crocodile", "Cyclops",
	"Dauthi", "Demon", "Deserter", "Devil", "Djinn", "Dragon", "Drake",
	"Dreadnought", "Drone", "Druid", "Dryad", "Dwarf", "Efreet", "Elder",
	"Eldrazi", "Elemental", "Elephant", "Elf", "Elk", "Eye", "Faerie",
	"Ferret", "Fish", "Flagbearer", "Fox", "Frog", "Fungus", "Gargoyle",
	"Germ", "Giant", "Gnome", "Goat", "Goblin", "Golem", "Gorgon",
	"Graveborn", "Gremlin", "Griffin", "Hag", "Harpy", "Hellion",
	"Hippo", "Hippogriff", "Homarid", "Homunculus", "Horror", "Horse",
	"Hound", "Human", "Hydra", "Hyena", "Illusion", "Imp", "Incarnation",
	"Insect", "Jellyfish", "Juggernaut", "Kavu", "Kirin", "Kithkin", "Knight",
	"Kobold", "Kor", "Kraken", "Lammasu", "Leech", "Leviathan", "Lhurgoyf",
	"Licid", "Lizard", "Manticore", "Masticore", "Mercenary", "Merfolk",
	"Metathran", "Minion", "Minotaur", "Monger", "Mongoose", "Monk", "Moonfolk", 
	"Mutant", "Myr", "Mystic", "Nautilus", "Nephilim", "Nightmare",
	"Nightstalker", "Ninja", "Noggle", "Nomad", "Octopus", "Ogre", "Ooze",
	"Orb", "Orc", "Orgg", "Ouphe", "Ox", "Oyster", "Pegasus", "Pentavite",
	"Pest", "Phelddagrif", "Phoenix", "Pincher", "Pirate", "Plant", "Praetor", 
	"Prism", "Rabbit", "Rat", "Rebel", "Reflection", "Rhino", "Rigger", "Rogue",
	"Salamander", "Samurai", "Sand", "Saproling", "Satyr", "Scarecrow",
	"Scorpion", "Scout", "Serf", "Serpent", "Shade", "Shaman", "Shapeshifter",
	"Sheep", "Siren", "Skeleton", "Slith", "Sliver", "Slug", "Snake", "Soldier",
	"Soltari", "Spawn", "Specter", "Spellshaper", "Sphinx", "Spider", "Spike",
	"Spirit", "Splinter", "Sponge", "Squid", "Squirrel", "Starfish", "Surrakar",
	"Survivor", "Tetravite", "Thalakos", "Thopter", "Thrull", "Treefolk",
	"Triskelavite", "Troll", "Turtle", "Unicorn", "Vampire", "Vedalken",
	"Viashino", "Volver", "Wall", "Warrior", "Weird", "Werewolf", "Whale",
	"Wizard", "Wolf", "Wolverine", "Wombat", "Worm", "Wraith", "Wurm", "Yeti",
	"Zombie", "Zubera"])

tribal_type = creature_type

artifact_type = or_cl (["Contraption", "Equipment", "Fortification"])

planeswalker_type = or_cl \
	(["Ajani", "Bolas", "Chandra", "Elspeth",
	"Garruk", "Gideon", "Jace", "Karn", "Koth",
	"Liliana", "Nissa", "Sarkhan", "Sorin",
	"Tamiyo", "Tezzeret", "Tibalt", "Venser"])

enchantment_type = or_cl (["Aura", "Curse", "Shrine"])

spell_type = or_cl (["Arcane", "Trap"])

a_subtype = spell_type | enchantment_type | planeswalker_type | artifact_type | creature_type | land_type

a_creature = or_cl (["Creature", "Creatures"])

a_token = or_cl (["Token", "Tokens"])

a_tribal = or_cl (["Tribal", "Tribals"])

an_instant = or_cl (["Instant", "Instants"])

a_sorcery = or_cl (["Sorcery", "Sorceries"])

a_land = or_cl (["Land", "Lands"])

an_artifact = or_cl (["Artifact", "Artifacts"])

an_enchantment = or_cl (["Enchantment", "Enchantments"])

a_planeswalker = or_cl (["Planeswalker", "Planeswalkers"])

a_type = a_creature | a_token | a_tribal | an_instant | a_sorcery \
					| a_land | an_artifact | an_enchantment | a_planeswalker

a_supertype = or_cl	(["Basic", "Legendary", "Snow", "World"])

a_nontype = Group(CaselessLiteral("Non") + (a_supertype | a_subtype | a_type))

supertypes = OneOrMore(a_supertype)

types = OneOrMore(a_type)

subtypes = OneOrMore(a_subtype)

cardtypeline = Group(
	Optional(supertypes)
	+ types
	+ Optional(Suppress(dash) + subtypes)
)