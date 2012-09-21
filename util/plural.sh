#!/bin/sh
#!/bin/sh

INPUT=$1
OUTPUT=$1.plural

cat $INPUT | \
gsed -E -n 's/^([^,]+)[,]?$/\1 \1s/p' > $OUTPUT