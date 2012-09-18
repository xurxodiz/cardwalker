#!/bin/sh

INPUT=$1
OUTPUT=$1.decl

cat $INPUT | \
gsed -E 's/(.+) << (.*)$/\1 = Forward\(\)/' > $OUTPUT