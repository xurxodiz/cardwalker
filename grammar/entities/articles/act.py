from ...functions.xml.deff import *

def change(s,l,t):
	if "+" == t[0]:
		return wrap("increaseby", t[1])
	elif "-" == t[0]:
		return wrap("decreaseby", t[1])
	else: # doesn't matter, it's zero
		return wrap("increaseby", wrap("num", "0"))

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