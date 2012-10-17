from ...functions.xml.deff import *

def your(s,l,t):
	return emptytag("you")

def its(s,l,t):
	return emptytag("it")

def their(s,l,t):
	return emptytag("they")

def his(s,l,t):
	return emptytag("he")

def singleposs(s,l,t):
	return wrap("possesion", t)

def who(s,l,t):
	return emptytag(t[0])

def person(s,l,t):
	return wrap("person", t)

def people(s,l,t):
	return wrap("people", t)

def personposs(s,l,t):
	return wrap("possession", t[0])

def peoplecontrol(s,l,t):
	return wrap("control", t[0])

def undercontrol(s,l,t):
	return wrap("control", t[1])