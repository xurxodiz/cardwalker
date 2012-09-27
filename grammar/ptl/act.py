from pyparsing import *

from ..functions.xml.deff import wrap, concat

def ptmod(s,l,t):
	p = wrap("power", t[0])
	t = wrap("toughness", t[1])
	wrap("ptmod", [p, t])

def loyaltymod(s,l,t):
	return wrap("loyaltymod", t[0])

def loyaltystart(s,l,t):
	return wrap("loyalty", t[0])

def ptstart(s,l,t):
	p = wrap("power", t[0])
	t = wrap("toughness", t[1])
	return wrap("pt", [p, t])
