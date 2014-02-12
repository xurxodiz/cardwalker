#!/bin/sh
#!/bin/sh

## Creates a decl.py file from a deff.py file

INPUT=$1
OUTPUT=$1.decl

cat $INPUT | \
gsed -E -n '
s/(.+) << (.*)$/\1 = Forward\(\)/p
/^$/p' > $OUTPUT