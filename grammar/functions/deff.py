from pyparsing import *

from ..constants.punctuation.deff import COMMA
from ..constants.connectors.deff import AND, OR

def delimitedListAnd(elem):
	return delimitedList(elem, ZeroOrMore(COMMA|AND))

def delimitedListOr(elem):
	return delimitedList(elem, OneOrMore(COMMA|OR))

def oneOfNamed(ssv):
	# ssv - space separated values
	return oneOf(ssv, True).setResultsName(ssv.split()[0])

def loadFromFile(path):
	with open(path) as f:
		return Or([oneOfNamed(line) for line in f.read().splitlines()])

def loadLinesFromFile(path):
	with open(path) as f:
		return Or([CaselessLiteral(line) for line in f.read().splitlines()])