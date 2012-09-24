from ...basic.functions.xml.deff import wrap, emptytag, lowername

def protection(s,l,t):
	return None #wrap("protection", t)

def landwalk(s,l,t):
	return None #wrap("walk", t)

def basic_keyword(s,l,t):
	return None #emptytag(lowername(t))

def number_keyword(s,l,t):
	return None #wrap(lowername(t), wrap("number", t[1]))

def cycling(s,l,t):
	return wrap("cycling", t[0])

def costed_keyword(s,l,t):
	return None #t[0]

def keywords(s,l,t):
	return None #wrap("keywords", t)