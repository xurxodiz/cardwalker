from pyparsing import *

from ...constants.articles.deff import THE
from ...constants.zones.deff import GRAVEYARD, BATTLEFIELD, HAND, LIBRARY, TOP, BOTTOM
from ...constants.prepositions.deff import UPTO, OF, IN, FROM
from ..articles.deff import det
from ..people.deff import peopleposs, peoplecontrol

from decl import *

detzone << (det|peopleposs) + (GRAVEYARD|HAND|LIBRARY)
thebattlefield << THE + BATTLEFIELD
thetopbottomoflibrary << THE + (TOP|BOTTOM) + OF + peopleposs + LIBRARY

zone << (detzone|thebattlefield|thetopbottomoflibrary)

inzone << IN + zone
ofzone << OF + zone
fromzone << FROM + zone

where << (peoplecontrol|inzone|ofzone|fromzone)