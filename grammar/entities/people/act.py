from ...functions.xml.deff import *

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

def peoplecontrol(s,l,t):
	return wrap("control", t[0])

def undercontrol(s,l,t):
	return wrap("control", t[1])