from grammar.card.deff import card
from lxml import etree
import sys
import re

total, cleared = 0, 0

def main():
    global cleared, total

    single = (len(sys.argv) > 1)

    if single:
        path = "oracle/card.txt"
    else:
        path = "oracle/workingset.txt"

    with open(path, "r") as f:
        storage = ""

        for line in f:
            storage += line
            if not line.strip():
                name = storage.splitlines()[0]
                # with this hack we get the ~ reference and save LOTS of computation time
                sto = name + "\n"
                for line in storage.splitlines()[1:]:
                    sto += re.sub("\\b" + name + "\\b(?!$)", "~", line) + "\n"
                if single:
                    deep_parse(sto)
                else:
                    parse(name, sto)
                storage = ""

        if not single:
            print "Parsed %s out of %s" % (cleared, total)


def parse(name, s):
    global cleared, total
    total += 1

    try:
        """tree = "".join(card.parseString(s))
        root = etree.fromstring(tree)
        r = root.xpath('//name')
        print "Parsed: %s" % r[0].text"""

        card.parseString(s)
        print "Parsed: %s" % name
        cleared += 1

    except:
        try:
            print "Error parsing: %s" % name
        except:
            print "Error"


def deep_parse(s):
    tree = "".join(card.parseString(s))
    root = etree.fromstring(tree)
    print(etree.tostring(root, pretty_print=True))


if __name__ == '__main__':
    main()