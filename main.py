from grammar.card import *

with open("oracle/card.txt", "r") as f:
    res = card.parseString(f.read())
    print res