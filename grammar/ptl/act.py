from pyparsing import *

def change(s,l,t):
	if "+" == t[0]:
		return "<increaseby>%s</increaseby>" % t[1]
	else:
		return "<decreaseby>%s</decreaseby>" % t[1]

def amount(s,l,t):
	if 2 == len(t):
		return "<sum><base>%s</base>%s</sum>" % (t[0], t[1])

	else:
		if "X" == t[0]:
			return "<refx />"
		else:
			return int(t[0])

def ptmod(s,l,t):
	return "<ptmod><power>%s</power>" \
			+ "<toughness>%s</toughness></ptmod>" % (t[0], t[1])

def loyaltymod(s,l,t):
	return "<loyaltymod>%s</loyaltymod>" % t[0]

def loyaltystart(s,l,t):
	return "<loyalty>%s</loyalty>" % t[0]

def ptstart(s,l,t):
	return "<pt><power>%s</power><toughness>%s</toughness></pt>" % (t[0], t[1])
