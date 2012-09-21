from ...basic.functions.deff import *

def protection(s,l,t):
	return wrap("protection", t)

def landwalk(s,l,t):
	return wrap("walk", t)

def basic_keyword(s,l,t):
	return "<keyword name='%s' />" % lowername(t)

def number_keyword(s,l,t):
	#name = lowername(t)
	return "<keyword name='%s'><number>%s</number></keyword>" % (t[0], t[1])

def costed_keyword(s,l,t):
	return None

def keywords(s,l,t):
	return wrap("keywords", t)