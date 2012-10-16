from pyparsing import *

from ..people.deff import peopleposs
from ...constants.resources.deff import LIFE, TOTAL, SIZE
from ...constants.zones.deff import HAND

from decl import *

lifetotal << peopleposs + LIFE + TOTAL
handsize << peopleposs + HAND + SIZE

resource << (lifetotal|handsize)