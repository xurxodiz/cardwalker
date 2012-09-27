from pyparsing import *

change = Forward()
amount = Forward()

uptoamount = Forward()
an = Forward()
another = Forward()
alll = Forward()

quantity = Forward()

target = Forward()
quantitytarget = Forward()
this = Forward()
that = Forward()
other = Forward()
each = Forward()
its = Forward()
the = Forward()

det = Forward()

people = Forward()

your = Forward()
their = Forward()
his = Forward()
peoploss = Forward()

peopleposs = Forward()

detzone = Forward()
thebattlefield = Forward()
thetopoflibrary = Forward()

zone = Forward()

peoplecontrol = Forward()
inzone = Forward()
ofzone = Forward()
fromzone = Forward()

where = Forward()

lifetotal = Forward()
handsize = Forward()

resource = Forward()

adjective = Forward()

andadjectives = Forward()
oradjectives = Forward()
consadjectives = Forward()

adjectives = Forward()

andsubtypes = Forward()
orsubtypes = Forward()

thesubtypes = Forward()

andtypes = Forward()
ortypes = Forward()
constypes = Forward()

thetypes = Forward()

andconcepts = Forward()
orconcepts = Forward()
consconcepts = Forward()

theconcepts = Forward()

baseobject_ = Forward()

object_ = Forward()

it = Forward()

objects = Forward()

mayer = Forward()
subject = Forward()