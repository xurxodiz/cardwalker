from ...functions.xml.deff import *

def until(s,l,t):
	return wrap("until", wrap("turn", emptytag("end")))
	
def havekeywords(s,l,t):
	return t[1]

def getptmod(s,l,t):
	return t[1]

def gaincontrol(s,l,t):
	return wrap("control", t[3])

def cantblock(s,l,t):
	return wrap("cant", emptytag("block"))

def mustattack(s,l,t):
	return wrap("must", emptytag("attack"))

def properties(s,l,t):
	return wrap("properties", t)

def continuous(s,l,t):
	return wrap("continuous", t)