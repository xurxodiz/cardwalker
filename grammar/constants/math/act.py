from ...functions.xml import *

def xvar(s,l,t):
	return emptytag("refx")

def num(s,l,t):
	return wrap("num", str(t[0]))

def fullnum(s,l,t):
	if "one" == t[0]:
		return num(s,l,[1])
	if "two" == t[0]:
		return num(s,l,[2])
	if "three" == t[0]:
		return num(s,l,[3])
	if "four" == t[0]:
		return num(s,l,[4])
	if "five" == t[0]:
		return num(s,l,[5])
	if "six" == t[0]:
		return num(s,l,[6])
	if "seven" == t[0]:
		return num(s,l,[7])
	if "eight" == t[0]:
		return num(s,l,[8])
	if "nine" == t[0]:
		return num(s,l,[9])
