from ...functions.xml.deff import *

def concept(s,l,t):
	return emptytag(t[0])

def ornoun(s,l,t):
	return wrap("option", t)

def basething(s,l,t):
	return wrap("base", t)

def thing(s,l,t):
	return wrap("thing", t)

def orthings(s,l,t):
	return wrap("option", t)

def it(s,l,t):
	return emptytag("it")

def they(s,l,t):
	return emptytag("they")

def name(s,l,t):
  return wrap("name", t)

def thiscard(s,l,t):
  return emptytag("thiscard")

def named(s,l,t):
  return wrap("named", t[1])