from ..basic.functions.deff import *

def type_(s,l,t):
	return "<type type='%s' />" % lowername(t)

def supertype(s,l,t):
	return "<supertype type='%s' />" % lowername(t)

def subtype(s,l,t):
	return "<subtype type='%s' />" % lowername(t)

def nontype(s,l,t):
	return wrap("not", [t[1]])

def supertypes(s,l,t):
	return wrap("supertypes", t)

def types(s,l,t):
	return wrap("types", t)

def subtypes(s,l,t):
	return wrap("subtypes", t)

def cardtypeline(s,l,t):
	return wrap("typeline", t)