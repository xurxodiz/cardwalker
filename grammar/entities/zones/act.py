from ...functions.xml.deff import *

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

def inzone(s,l,t):
	return t[1]

def ofzone(s,l,t):
	return t[1]

def fromzone(s,l,t):
	return t[1]
