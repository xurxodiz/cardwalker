from ...functions.xml.deff import *

def topnum(s,l,t):
	return wrap(t[0], t[1])

def attacking(s,l,t):
	return emptytag("attacking")

def blocking(s,l,t):
	return emptytag("blocking")

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