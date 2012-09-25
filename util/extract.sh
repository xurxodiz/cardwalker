#!/bin/sh

# if no parameters, we look for Magic 2013
case $# in 
	0) EXP="M13";;
	*) EXP=$@;;
esac;

echo "Extracting cards from sets:" $EXP

# we prepare the regex by substituting spaces for |
# (alternative operator)
OR=(${EXP/ /\|})
INPUT=../oracle/allsets.txt
OUTPUT=../oracle/workingset.txt

# now, we open the master file
# feed to a sed that buffers a card and check the expansion
# outputs it if in the expansion
# the second sed erases trailing blank lines on the stream (not inter-card)
# finally, we dump it to output file

cat $INPUT \
| sed -E -n '
/^$/! {
	# if nonempty, store lines until...
	H
}
/^$/ {
	# ... empty line -> end of card
	# restore stored lines into pattern space
	x
	# if it belongs to any of the expansions
	/[[:<:]]'$OR'[[:>:]]/ {
		# (fugly word boundary syntax for osx sed)
		# print it
		p
	}
	# and delete it from pattern space
	d
	# exchange pattern space and store space (effectively empties storage)
	x
}' \
| sed '/./,$!d' \
> $OUTPUT

# extra line break for proper format
# each card is known to be finished by a \n
# so lack of this could make the last card be skipped
echo "" >> $OUTPUT
