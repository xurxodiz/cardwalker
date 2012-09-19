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

PLUS << Literal("+")
MINUS << Literal("-")

XVAR << (Keyword("X") | Keyword("*"))

DIGIT << oneOf("0 1 2 3 4 5 6 7 8 9")
NUM << Combine(OneOrMore(DIGIT))
FULLNUM << oneOf ("one two three four five six seven eight nine", caseless=True)

UPPERCASE << oneOf ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

AND << CaselessLiteral("and")
OR << CaselessLiteral("or")

NON << CaselessLiteral("Non")

THIS << CaselessKeyword("this")
THAT << CaselessKeyword("that")
IT << CaselessLiteral("it")

AN << oneOf ("a an", caseless=True)
THE << CaselessLiteral("the")
OTHER << CaselessLiteral("other")
ANOTHER << CaselessLiteral("another")
HIS << CaselessLiteral("his or her")
ALL << CaselessLiteral("all")
EACH << CaselessLiteral("each")
ITS << oneOf("its their", caseless=True)
YOUR << CaselessLiteral("your")
THEIR << CaselessLiteral("their")
POSS << (CaselessLiteral("'s") | APOS)

WHEN << oneOf ("when whenever", caseless=True)
WHERE << CaselessLiteral("where")
TARGET << CaselessLiteral("target")
MAY << CaselessLiteral("may")
TO << CaselessLiteral("to")
UPTO << CaselessLiteral("up to")
OF << CaselessLiteral("of")
IN << CaselessLiteral("in")
ON << CaselessLiteral("on")
ONTO << CaselessLiteral("onto")
INTO << CaselessLiteral("into")
WITH << CaselessLiteral("with")
FROM << CaselessLiteral("from")
BY << CaselessLiteral("by")
AT << CaselessLiteral("at")
FOR << CaselessLiteral("for")
UNTIL << CaselessLiteral("until")
UNDER << CaselessLiteral("under")
NEXT << CaselessLiteral("next")
WITH << CaselessLiteral("with")
EQUAL << CaselessLiteral("equal")

BE << oneOf("is are", caseless=True)
HAVE << oneOf("has have", caseless=True)
GET << oneOf("get gets", caseless=True)
CANT << CaselessLiteral("can't")
MUST << CaselessLiteral("must")

DESTROY << oneOf("destroy destroys destroyed", caseless=True)
EXILE << oneOf("exile exiles exiled", caseless=True)
GAIN << oneOf("gain gains gained", caseless=True)
LOSE << oneOf("lose loses lost", caseless=True)
TAP << oneOf("tap taps", caseless=True)
UNTAP << oneOf("untap untaps untapped", caseless=True)
DISCARD << oneOf("discard discards discard", caseless=True)
SACRIFICE << oneOf("sacrifice sacrifices sacrificed", caseless=True)
DRAW << oneOf("draw draws drawn", caseless=True)
DEAL << oneOf("deal deals dealt", caseless=True)
PAY << oneOf("pay pays paid", caseless=True)
PUT << oneOf("put puts", caseless=True)
ATTACK << oneOf("attack attacks attacking", caseless=True)
BLOCK << oneOf("block blocks blocking", caseless=True)
BECOME << oneOf("become becomes", caseless=True)
REDUCE << oneOf("reduce reduced reduces", caseless=True)
RETURN << oneOf("return returned returns", caseless=True)
ENTER << oneOf("enter enters", caseless=True)
LEAVE << oneOf("leave leaves", caseless=True)
DIE << oneOf("die dies died", caseless=True)
PREVENT << oneOf("prevent prevents prevented", caseless=True)
ADD << oneOf("add adds added", caseless=True)
REGENERATE << oneOf("regenerate regenerates regenerated", caseless=True)
CONTROL << oneOf("control controls", caseless=True)

SPELL << oneOf("spell spells", caseless=True)
PERMANENT << oneOf("permanent permanents", caseless=True)
CARD << oneOf("card cards", caseless=True)
ABILITY << oneOf("ability abilities", caseless=True)
COUNTER << CaselessLiteral("counter")
COUNTERSPELL << oneOf("counter counters", caseless=True)

CONTROLLER << oneOf("controller controllers", caseless=True)
OWNER << oneOf("owner owners", caseless=True)
YOU << CaselessLiteral("you")
PLAYER << oneOf("player players", caseless=True)
OPPONENT << oneOf("opponent opponents", caseless=True)

HAND << oneOf("hand hands", caseless=True)
GRAVEYARD << oneOf("graveyard graveyards", caseless=True)
LIBRARY << oneOf("library libraries", caseless=True)
EXILE << CaselessLiteral("exile")
BATTLEFIELD << CaselessLiteral("battlefield")

ATRANDOM << CaselessLiteral("at random")
ALONE << CaselessLiteral("alone")

TOTAL << CaselessLiteral("total")
SIZE << CaselessLiteral("size")
NUMBER << CaselessLiteral("number")

BEGINNING << CaselessLiteral("beginning")
END << CaselessLiteral("end")
TOP << CaselessLiteral("top")
BOTTOM << CaselessLiteral("bottom")

TURN << CaselessLiteral("turn")
UPKEEP << CaselessLiteral("upkeep")
DRAWSTEP << CaselessLiteral("draw step")
PRECOMBAT << CaselessLiteral("first main phase")
COMBAT << CaselessLiteral("combat phase")
POSCOMBAT << CaselessLiteral("second main phase")

DAMAGE << CaselessLiteral("damage")
LIFE << CaselessLiteral("life")
MANA << CaselessLiteral("mana")
POOL << CaselessLiteral("pool")
SOURCE << oneOf("source sources", caseless=True)
