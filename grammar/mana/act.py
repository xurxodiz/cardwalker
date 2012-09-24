from pyparsing import *

from ..basic.functions.xml.deff import emptytag, wrap

def colorname(s,l,t):
	if "white" == t[0]:
		return emptytag("W")
	elif "blue" == t[0]:
		return emptytag("U")
	elif "black" == t[0]:
		return emptytag("B")
	elif "red" == t[0]:
		return emptytag("R")
	elif "green" == t[0]:
		return emptytag("G")

def noncolorname(s,l,t):
	return wrap("not", [colorname(s,l,t)])

def abschar(s,l,t):
	if "colorless" == t[1]:
		return "<color color='colorless' />"
	elif "colored" == t[1]:
		return "<color color='colored' />"
	elif "multicolored" == t[1]:
		return "<color color='multi' />"
	else: # monocolored
		return "<color colored='mono' />"

def manasymbol(s,l,t):
	return emptytag(t[0])

def snowsymbol(s,l,t):
	return emptytag("S")

def tapsymbol(s,l,t):
	return emptytag("tap")

def untapsymbol(s,l,t):
	return emptytag("untap")

def physymbol(s,l,t):
	paylife = wrap("life", wrap("num", ["2"]))
	return wrap("option", [paylife, t[0]])

def hybsymbol(s,l,t):
	paymana = wrap("mana", wrap("colorless", t[0]))
	return wrap("option", [paymana, t[1]])

def chybsymbol(s,l,t):
	return wrap("option", t)

def numcost(s,l,t):
	return wrap("colorless", t)

def xcost(s,l,t):
	return wrap("colorless", t)

def manapayment(s,l,t):
	return wrap("pay", wrap("mana", t))

def cardcost(s,l,t):
	return wrap("cost", wrap("mana", t))