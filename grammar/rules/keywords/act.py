from ...functions.xml.deff import wrap, emptytag, lowername

def protection(s,l,t):
	return wrap("protection", t)

def landwalk(s,l,t):
	return wrap("walk", t)

def basic_keyword(s,l,t):
	return emptytag(lowername(t))

def number_keyword(s,l,t):
	return wrap(lowername(t), wrap("number", t[1]))

def cycling(s,l,t):
	return wrap("cycling", t)

def costed_keyword(s,l,t):
	return emptytag(t[0])