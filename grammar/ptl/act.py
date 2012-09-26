from pyparsing import *

from ..functions.xml.deff import wrap, concat

def change(s,l,t):
	if "+" == t[0]:
		return wrap("increaseby", t[1])
	elif "-" == t[0]:
		return wrap("decreaseby", t[1])
	else: # doesn't matter, it's zero
		return wrap("increaseby", "0")

def amount(s,l,t):
	return concat(t)

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
