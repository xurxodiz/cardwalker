from ..functions.xml.deff import wrap, lowername, emptytag

def name(s,l,t):
	return wrap("name", t[0])

def type_(s,l,t):
	return emptytag(lowername(t))

def supertype(s,l,t):
	return emptytag(lowername(t))

def subtype(s,l,t):
	return emptytag(lowername(t))

def nontype(s,l,t):
	return wrap("not", t[1])