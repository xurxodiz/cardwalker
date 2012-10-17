from ..functions.xml.deff import *

def rule(s,l,t):
	return wrap("rule", t)

def rulelist(s,l,t):
	return wrap("set", t)