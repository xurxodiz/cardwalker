from pyparsing import *

from decl import *

EOL << LineEnd().suppress()

QUOTE << Suppress("\"")
COMMA << Suppress(",")
POINT << Suppress(".")

LPAREN << Suppress("(")
RPAREN << Suppress(")")
LBRACE << Suppress("{")
RBRACE << Suppress("}")
LBRACKET << Suppress("[")
RBRACKET << Suppress("]")
SLASH << Suppress("/")
DASH << Suppress(Word("-"))
COLON << Suppress(":")

APOS << Literal("'")