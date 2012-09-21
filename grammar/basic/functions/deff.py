from pyparsing import *

from ..constants.deff import COMMA, AND

def delimitedListAnd(elem):
	lim = Optional(COMMA+AND|COMMA|AND)
	return delimitedList(elem, lim)

def oneOfNamed(ssv):
	return oneOf(ssv, True).setResultsName(ssv.split()[0])

def load_from_file(path):
	with open(path) as f:
		return Or([oneOfNamed(line) for line in f.read().splitlines()])

def wrap(tag, lst):
	return "<%s>%s</%s>" % (tag.lower(), "".join(lst), tag.lower())

def emptytag(tag):
	return "<%s />" % tag.lower()

def lowername(dct):
	return dct.keys()[0].lower()

"""
def or_cl(lst):
	return Or(map(CaselessLiteral, lst))

def or_l(lst):
	return Or(map(Literal, lst))

def or_cs(lst):
	return Suppress(or_cl(lst)) #Or(map(Suppress, map(CaselessLiteral, lst)))

def delimitedListOr(elem):
	helper = Suppress(OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))

def delimitedListAndOr(elem):
	helper = Suppress(AND|OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))
"""