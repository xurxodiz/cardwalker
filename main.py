from grammar.card.deff import card
import sys

total, cleared = 0, 0

single = (len(sys.argv) > 1)

if single:
    path = "oracle/card.txt"
else:
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
            if single:
                deep_parse(storage)
            else:
                parse(storage)
            storage = ""
        else:
            storage += line
    if not single:
        print "Passed %s out of %s" % (cleared, total)