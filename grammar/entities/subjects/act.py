from ...functions.xml.deff import *

def mayer(s,l,t):
	if len(t) > 2:
		may = wrap("may", t[4])
	elif len(t) == 2:
		may = emptytag("may")
	return concat([t[0], may])

def subject(s,l,t):
	return wrap("subject", t[0])