from pyparsing import *

def load_from_file(path, ignoreCase=True):
	with open(path) as f:
		return oneOf(" ".join(f.read().splitlines()), ignoreCase)

"""
def or_cl(lst):
	return Or(map(CaselessLiteral, lst))

def or_l(lst):
	return Or(map(Literal, lst))

def or_cs(lst):
	return Suppress(or_cl(lst)) #Or(map(Suppress, map(CaselessLiteral, lst)))

def delimitedListAnd(elem):
	helper = Suppress(AND) + elem | elem
	return delimitedList(helper, Optional(COMMA))

def delimitedListOr(elem):
	helper = Suppress(OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))

def delimitedListAndOr(elem):
	helper = Suppress(AND|OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))
"""