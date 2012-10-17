from pyparsing import *

from ..people.deff import people
from ..things.deff import things
from ...constants.verbs.deff import MAY, HAVE

from decl import *

objects = (people|things)

mayhave << people + MAY + HAVE + objects
may << people + MAY

subjects << (mayhave|may|objects)