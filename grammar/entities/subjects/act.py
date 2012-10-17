from ...functions.xml.deff import *

def orobjects(s,l,t):
	return wrap("option", t)

def objects(s,l,t):
	return wrap("objects", t)

def mayhave(s,l,t):
	return concat(t[0], wrap("may", t[4]))

def may(s,l,t):
	return concat(t[0], emptytag("may"))

def subjects(s,l,t):
	return wrap("subjects", t)