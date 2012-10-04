from ...functions.xml.deff import *

def turn(s,l,t):
	return emptytag("turn")

def upkeep(s,l,t):
	return emptytag("upkeep")

def drawstep(s,l,t):
	return emptytag("drawstep")

def precombat(s,l,t):
	return emptytag("precombat")

def combat(s,l,t):
	return emptytag("combat")

def poscombat(s,l,t):
	return emptytag("poscombat")

def until(s,l,t):
	return wrap("until", wrap("turn", emptytag("end")))
	
def havekeywords(s,l,t):
	return wrap("keywords", t[1:])

def getptmod(s,l,t):
	return t[1]

def beindestructible(s,l,t):
	return emptytag("indestructible")

def beunblockable(s,l,t):
	return emptytag("unblockable")

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