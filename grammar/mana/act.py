from pyparsing import *

def colorname(s,l,t):
	if "white" == t[0]:
		color = "W"
	elif "blue" == t[0]:
		color = "U"
	elif "black" == t[0]:
		color = "B"
	elif "red" == t[0]:
		color = "R"
	else: # green
		color = "G"
	return "<color color='%s' />" % color

def noncolorname(s,l,t):
	if "white" == t[1]:
		color = "W"
	elif "blue" == t[1]:
		color = "U"
	elif "black" == t[1]:
		color = "B"
	elif "red" == t[1]:
		color = "R"
	else: # green
		color = "G"
	return "<color color='%s' match='false' />" % color

def abschar(s,l,t):
	if "colorless" == t[1]:
		return "<color colorless='true' />"
	elif "colored" == t[1]:
		return "<color colorless='false' />"
	elif "multicolored" == t[1]:
		return "<color muticolored='true' />"
	else: # monocolored
		return "<color multicolored='false' />"

def manasymbol(s,l,t):
	return "<mana color='%s' />" % t[0]

def snowsymbol(s,l,t):
	return "<mana color='S' />"

def tapsymbol(s,l,t):
	return "<tap />"

def untapsymbol(s,l,t):
	return "<untap />"

def physymbol(s,l,t):
	cless = "<pay resource='life' amount='2' />"
	return "<option>%s%s</option>" % (cless, t[0])

def hybsymbol(s,l,t):
	cless = "<mana color='colorless' amount='2' />"
	return "<option>%s%s</option>" % (cless, t[1])

def chybsymbol(s,l,t):
	return "<option>%s%s</option>" % (t[0],t[1])

def numcost(s,l,t):
	return "<mana color='colorless' amount='%s' />" % t[0]

def xcost(s,l,t):
	return "<mana color='colorless' amount='X' />"

def manapayment(s,l,t):
	return "<pay resource='mana'>" + "".join(t.asList()) + "</pay>"

def cardcost(s,l,t):
	return "<cost>" + "".join(t.asList()) + "</cost>"