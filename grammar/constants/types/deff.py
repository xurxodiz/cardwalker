from pyparsing import *

from ...functions.deff import loadLinesFromFile, loadFromFile

from decl import *

CARDNAME << loadLinesFromFile("oracle/ref/names.txt")
SUPERTYPE << loadFromFile("oracle/ref/supertypes.txt")
TYPE_ << loadFromFile("oracle/ref/types.txt")
BASICLANDTYPE << loadFromFile("oracle/ref/basic_land_types.txt")
OTHERLANDTYPE << loadFromFile("oracle/ref/other_land_types.txt")
CREATURETYPE << loadFromFile("oracle/ref/creature_types.txt")
ARTIFACTTYPE << loadFromFile("oracle/ref/artifact_types.txt")
PLANESWALKERTYPE << loadFromFile("oracle/ref/planeswalker_types.txt")
ENCHANTMENTTYPE << loadFromFile("oracle/ref/enchantment_types.txt")
SPELLTYPE << loadFromFile("oracle/ref/spell_types.txt")