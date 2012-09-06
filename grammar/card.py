from pyparsing import *
from basic import *
from types import *
from expansions import *
from pt import *
from mana import *
from rules import *

card = (cardname
	+ cardcost
	+ cardtypeline
	+ Optional(cardpt)
	+ Optional(cardrules)
	+ cardexpansions
)