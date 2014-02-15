#!/bin/sh

## Creates a list of all the cardnames in Magic

echo "Extracting names..."

INPUT=oracle/allsets.txt
OUTPUT=oracle/ref/names.txt

# if first line, print name of first card
# if end of card, print next line (name of next card)
cat $INPUT \
| sed -E -n '
1 {
	p
}
/^$/ {
	n
	p
}' \
| sed '/^$/d' | sed -n '1!G;h;$p' \
> $OUTPUT
