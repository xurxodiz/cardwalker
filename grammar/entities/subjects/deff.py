from pyparsing import *

from ..people.deff import people
from ..objects.deff import objects
from ..resources.deff import resource
from ...constants.verbs.deff import MAY, HAVE

from decl import *

mayer << people + MAY + Optional(HAVE + (people|objects))
subject << (resource|mayer|people|objects)