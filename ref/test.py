import ebnf_

with open('example.ebnf', 'r') as gr:
	t = ebnf_.parse(gr.read())

print t[0]

#with open('pascal.txt', 'r') as p:
	#print t['block'].parseString(p.read())
