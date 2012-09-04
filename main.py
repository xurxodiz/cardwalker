from grammar.card import *

total, cleared = 0, 0

def parse(str):
    global cleared, total
    total += 1
    try:
        tree = card.parseString(str)
        print "Parsed: %s" % " ".join(tree[0])
        cleared += 1
    except:
        print "Error parsing: %s" % storage.splitlines()[0]

with open("oracle/workingset.txt", "r") as f:
    storage = ""

    for line in f:
        if not line.strip():
            parse(storage)
            storage = ""
        else:
            storage += line
    
    # for the last card on file
    parse(storage)
    print "%s out of %s" % (cleared, total)