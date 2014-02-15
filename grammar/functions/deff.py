from pyparsing import *

from ..constants.punctuation.deff import COMMA
from ..constants.connectors.deff import AND, OR

def delimitedListAnd(elem):
	return delimitedList(elem, OneOrMore(COMMA|AND))

def delimitedListOr(elem):
	return delimitedList(elem, OneOrMore(COMMA|OR))

def oneOfNamed(ssv):
	# ssv - space separated values
	lst = ssv.split()
	return MatchFirst(map(CaselessKeyword, lst)).setResultsName(lst[0])

def named(sstr):
	return CaselessLiteral(sstr).setResultsName(sstr.replace (" ", "_"))

def loadFromFile(path):
	with open(path) as f:
		return MatchFirst([oneOfNamed(line.strip()) for line in f.read().splitlines()])

def loadLinesFromFile(path):
	with open(path) as f:
		return MatchFirst([named(line.strip()) for line in f.read().splitlines()])