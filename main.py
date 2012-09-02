import grammar

with open("oracle/card.txt", "r") as f:
    res = grammar.card.parseString(f.read())
    print res