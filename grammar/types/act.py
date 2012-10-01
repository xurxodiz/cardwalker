from ..functions.xml.deff import wrap, lowername, emptytag

def cardname(s,l,t):
	return wrap("name", t[0])

def type_(s,l,t):
	return emptytag(lowername(t))

def supertype(s,l,t):
	return emptytag(lowername(t))

def subtype(s,l,t):
	return emptytag(lowername(t))

def nontype(s,l,t):
	return wrap("not", t[1])

def cardsupertypes(s,l,t):
	return wrap("supertypes", t)

def cardtypes(s,l,t):
	return wrap("types", t)

def cardsubtypes(s,l,t):
	return wrap("subtypes", t)

def cardtypeline(s,l,t):
	return wrap("typeline", t)