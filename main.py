from grammar.card.deff import card
from lxml import etree
import sys

total, cleared = 0, 0

single = (len(sys.argv) > 1)

if single:
    path = "oracle/card.txt"
else:
    path = "oracle/workingset.txt"

def parse(s):
    global cleared, total
    total += 1
    try:
        tree = card.parseString(s)
        print "Parsed: %s" % " ".join(tree[0])
        cleared += 1
    except:
        try:
            print "Error parsing: %s" % storage.splitlines()[0]
        except:
            print "Error"

def deep_parse(s):
    tree = "".join(card.parseString(s))
    root = etree.fromstring(tree)
    print(etree.tostring(root, pretty_print=True))

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