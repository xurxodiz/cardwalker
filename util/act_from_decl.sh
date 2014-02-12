#!/bin/sh
#!/bin/sh

## Creates an act.py file from a decl.py file

INPUT=$1
OUTPUT=$1.act

cat $INPUT | \
gsed -E '
s/(.+) = Forward\(\)$/\1 = Forward\(\).setParseAction\(act\.\1\)/
' > $OUTPUT