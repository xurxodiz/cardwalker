from ..functions.xml import wrap

def cardcost(s,l,t):
	return wrap("cost", t)

def cardsupertypes(s,l,t):
	return wrap("supertypes", t)

def cardtypes(s,l,t):
	return wrap("types", t)

def cardsubtypes(s,l,t):
	return wrap("subtypes", t)

def cardtypeline(s,l,t):
	return wrap("typeline", t)

def cardrules(s,l,t):
	return wrap("rules", t)

def cardexpansions(s,l,t):
	return wrap("expansions", t)

def card(s,l,t):
	return wrap("card", t)