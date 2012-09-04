from pyparsing import *

digit = Or(map(Literal, "0123456789"))
caps = Or(map(Literal,"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

number = OneOrMore(digit)

apostrophe = Literal("'")
asterisk = Literal("*")
plus = Literal("+")
minus = Literal("-")
comma = Literal(",")
point = Literal(".")
lparen = Literal("(")
rparen = Literal(")")
slash = Literal("/")
dash = Word("-")
_and = CaselessLiteral("and")
_or = CaselessLiteral("or")

def delimitedListAnd(elem):
	helper = _and + elem | elem
	return delimitedList(helper, comma)

def delimitedListOr(elem):
	helper = _or + elem | elem
	return delimitedList(helper, comma)

def delimitedListAndOr(elem):
	helper = (_and | _or) + elem | elem
	return delimitedList(helper, comma)