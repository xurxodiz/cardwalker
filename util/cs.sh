#!/bin/sh

INPUT=$1
OUTPUT=$2.new

sed -E '
s/or_c[sl][[:space:]]?\(\[\"(.*)\", \"(.*)\", \"(.*)\"\]\)/oneOf\(\"\1 \2 \3\"\, caseless=True)/g
s/or_c[sl][[:space:]]?\(\[\"(.*)\", \"(.*)\"\]\)/oneOf\(\"\1 \2"\, caseless=True)/g
s/or_c[sl][[:space:]]?\(\[\"(.*)\"\]\)/CaselessLiteral\(\"\1"\)/g
' <$INPUT >$OUTPUT