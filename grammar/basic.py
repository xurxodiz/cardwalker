from pyparsing import *

ParserElement.setDefaultWhitespaceChars(" \t")

AND = CaselessLiteral("and")
OR = CaselessLiteral("or")

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

EOL = LineEnd().suppress()

APOS = Literal("'")
ASTERISK = Literal("*")
PLUS = Literal("+")
MINUS = Literal("-")

QUOTE = Suppress("\"")
COMMA = Suppress(",")
POINT = Suppress(".")
LPAREN = Suppress("(")
RPAREN = Suppress(")")
SLASH = Suppress("/")
DASH = Suppress(Word("-"))

digit = or_cl ("0123456789")
caps = or_cl ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

number = OneOrMore(digit)

fullnumber = or_cl (["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])