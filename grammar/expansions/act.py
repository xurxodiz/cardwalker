from pyparsing import *

from ..functions.xml.deff import wrap

def frequency(s,l,t):
	return wrap("frequency", t)

def expcode(s,l,t):
	return wrap("code", t)

def expansion(s,l,t):
	return wrap("exp", t)
	
def cardexpansions(s,l,t):
	return wrap("expansions", t)