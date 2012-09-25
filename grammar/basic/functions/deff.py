from pyparsing import *

from ..constants.deff import COMMA, AND

def delimitedListAnd(elem):
	lim = (COMMA+AND|COMMA|AND)
	return delimitedList(elem, lim)

def oneOfNamed(ssv):
	# ssv - space separated values
	return oneOf(ssv, True).setResultsName(ssv.split()[0])

def loadFromFile(path):
	with open(path) as f:
		return Or([oneOfNamed(line) for line in f.read().splitlines()])

"""
def delimitedListOr(elem):
	helper = Suppress(OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))

def delimitedListAndOr(elem):
	helper = Suppress(AND|OR) + elem | elem
	return delimitedList(helper, Optional(COMMA))
"""