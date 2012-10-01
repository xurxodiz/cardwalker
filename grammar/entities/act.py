from pyparsing import *

from ..functions.xml.deff import *

def change(s,l,t):
	if "+" == t[0]:
		return wrap("increaseby", t[1])
	elif "-" == t[0]:
		return wrap("decreaseby", t[1])
	else: # doesn't matter, it's zero
		return wrap("increaseby", wrap("num", [0]))

def amount(s,l,t):
	return concat(t)

def uptoamount(s,l,t):
	return wrap("upto", t[1])

def an(s,l,t):
	return emptytag(t[0])

def another(s,l,t):
	return emptytag(t[0])

def alll(s,l,t):
	return emptytag(t[0])

def target(s,l,t):
	return emptytag(t[0])

def quantitytarget(s,l,t):
	return wrap("target", t[0])

def this(s,l,t):
	return emptytag(t[0])

def that(s,l,t):
	return emptytag(t[0])

def other(s,l,t):
	return emptytag(t[0])

def each(s,l,t):
	return emptytag(t[0])

def its(s,l,t):
	return emptytag(t[0])

def the(s,l,t):
	return emptytag(t[0])

def det(s,l,t):
	wrap("det", t)

def detpeople(s,l,t):
	det = wrap("det", t[0])
	return concat([det,t[1]])

def people(s,l,t):
	return wrap("people", t)

def your(s,l,t):
	return emptytag("your")

def their(s,l,t):
	return emptytag("their")

def his(s,l,t):
	return emptytag("his")

def peoploss(s,l,t):
	return wrap("belong", t[0])

def peopleposs(s,l,t):
	return wrap("possession", t[0])

def detzone(s,l,t):
	return wrap(t[1], t[0])

def thebattlefield(s,l,t):
	return emptytag(t[1])

def thetopbottomoflibrary(s,l,t):
	toporbottom = emptytag(t[1])
	who = t[4]
	return wrap(t[5], [who, toporbottom])

def zone(s,l,t):
	return wrap("zone", t)

def peoplecontrol(s,l,t):
	return wrap("control", t[0])

def inzone(s,l,t):
	return t[1]

def ofzone(s,l,t):
	return t[1]

def fromzone(s,l,t):
	return t[1]

def lifetotal(s,l,t):
	return wrap("lifetotal", t[0])

def handsize(s,l,t):
	return wrap("handsize", t[0])

def topnum(s,l,t):
	return wrap(t[0], t[1])

def tapped(s,l,t):
	return emptytag("tapped")

def untapped(s,l,t):
	return emptytag("untapped")

def enchanted(s,l,t):
	return emptytag("enchanted")

def equipped(s,l,t):
	return emptytag("equipped")

def exiled(s,l,t):
	return emptytag("exiled")

def sacrificed(s,l,t):
	return emptytag("sacrificed")

def haunted(s,l,t):
	return emptytag("haunted")

def oradjectives(s,l,t):
	return wrap("option", t)

def adjectives(s,l,t):
	return wrap("adjectives", t)

def ornoun(s,l,t):
	return wrap("option", t)

def baseobject_(s,l,t):
	return wrap("base", t)

def object_(s,l,t):
	return wrap("object", t)

def orobjects(s,l,t):
	return wrap("option", t)

def ordetobjects(s,l,t):
	return wrap("option", t)

def objects(s,l,t):
	return wrap("objects", t)

def mayer(s,l,t):
	if len(t) > 2:
		may = wrap("may", t[4])
	elif len(t) == 2:
		may = emptytag("may")
	return concat([t[0], may])

def subject(s,l,t):
	return wrap("subject", t[0])