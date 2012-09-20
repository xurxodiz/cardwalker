#!/bin/sh

INPUT=$1
OUTPUT=$1.decl

cat $INPUT | \
gsed -E -n 's/(.+) << (.*)$/\1 = Forward\(\)/p' > $OUTPUT