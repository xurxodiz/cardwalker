from pyparsing import *

from ..functions.xml.deff import *

def change(s,l,t):
	if "+" == t[0]:
		return wrap("increaseby", t[1])
	elif "-" == t[0]:
		return wrap("decreaseby", t[1])
	else: # doesn't matter, it's zero
		return wrap("increaseby", "0")

def amount(s,l,t):
	return concat(t)

