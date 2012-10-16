from ...functions.xml.deff import *

def ornoun(s,l,t):
	return wrap("option", t)

def baseobject_(s,l,t):
	return wrap("base", t)

def object_(s,l,t):
	return wrap("object", t)

def orobjects(s,l,t):
	return wrap("option", t)

def it(s,l,t):
	return emptytag("it")

def they(s,l,t):
	return emptytag("they")