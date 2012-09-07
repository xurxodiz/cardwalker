from grammar.card import *

total, cleared = 0, 0

path = "oracle/workingset.txt"

def parse(str):
    global cleared, total
    total += 1
    try:
        tree = card.parseString(str)
        print "Parsed: %s" % " ".join(tree[0])
        cleared += 1
    except:
        try:
            print "Error parsing: %s" % storage.splitlines()[0]
        except:
            print "Error"

def deep_parse(str):
    tree = card.parseString(str)
    print tree

with open(path, "r") as f:
    storage = ""

    for line in f:
        if not line.strip():
            parse(storage)
            storage = ""
        else:
            storage += line
    print "Passed %s out of %s" % (cleared, total)