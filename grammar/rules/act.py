from ..functions.xml.deff import *

def tapsymbol(s,l,t):
  return emptytag("tap")

def untapsymbol(s,l,t):
  return emptytag("untap")

def cost(s,l,t):
  return wrap("cost", t)

def activated(s,l,t):
  return wrap("activated", t)

def rule(s,l,t):
	return wrap("rule", t)

def rulelist(s,l,t):
	return wrap("set", t)