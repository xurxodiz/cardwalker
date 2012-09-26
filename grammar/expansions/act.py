from pyparsing import *

def expansions(s,l,t):
	return "<expansion code='%s' frequency='%s' />" % (t[0], t[1])
	
def cardexpansions(s,l,t):
	s = "<expansions>"
	for tt in t.asList():
		s += tt
	s += "</expansions>"
	return s