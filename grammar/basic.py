from pyparsing import *

def or_cl(lst):
	return Or(map(CaselessLiteral, lst))

def or_l(lst):
	return Or(map(Literal, lst))

digit = or_cl ("0123456789")
caps = or_cl ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

number = OneOrMore(digit)

fullnumber = or_cl (["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])

apostrophe = Literal("'")
asterisk = Literal("*")
plus = Literal("+")
minus = Literal("-")

comma = Suppress(",")
point = Suppress(".")
lparen = Suppress("(")
rparen = Suppress(")")
slash = Suppress("/")
dash = Suppress(Word("-"))

and_ = CaselessLiteral("and")
or_ = CaselessLiteral("or")

are = Suppress("is") | Suppress("are")
have = Suppress("has") | Suppress("have")
get = Suppress("get") | Suppress("gets")
from_ = Suppress("from")
an = Suppress("a") | Suppress("an")

when = or_cl(["when", "whenever"])

cardname = Group(Word(alphas + " '"))

def delimitedListAnd(elem):
	helper = Suppress(and_) + elem | elem
	return delimitedList(helper, Optional(comma))

def delimitedListOr(elem):
	helper = Suppress(or_) + elem | elem
	return delimitedList(helper, Optional(comma))

def delimitedListAndOr(elem):
	helper = Suppress(and_ | or_) + elem | elem
	return delimitedList(helper, Optional(comma))