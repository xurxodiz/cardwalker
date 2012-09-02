grammar Card;

options {
    language=Python;
}

card		: 	name NEWLINE
				cost NEWLINE
				typeline NEWLINE
				pt NEWLINE
				rulestext NEWLINE
				expansion NEWLINE
				NEWLINE
			;

name		:  	NAME
			;

cost		: 	(DIGIT* manacolor+ | DIGIT+)
			;

typeline	:	supertypes? types (SP DASH SP subtypes)?
			;

supertypes	:	supertype (SP supertype)*
			;

fragment supertype	: 	('Snow' | 'World' | 'Basic' | 'Legendary')
			;

types		:	type (SP type)*
			;

fragment type 		:	('Creature' | 'Land' | 'Instant'
				| 'Sorcery' | 'Tribal' | 'Planeswalker'
				| 'Enchantment' | 'Artifact')
			;

subtypes	:	subtype (SP subtype)*
			;

fragment subtype 	:	LETTER+
			;

pt 			:	DIGIT+ '/' DIGIT+
			;

rulestext	:	rule? (NEWLINE rule)*
			;

fragment rule 		:	TEXT
			;

fragment expansion	:	expcode '-' frequency
			;

fragment expcode	:	(DIGIT|LETTER) (DIGIT|LETTER) (DIGIT|LETTER)?
					;

fragment frequency	:	('M'|'R'|'U'|'C'|'S'|'L'|'T')
					;

fragment mana 		:	manacolor | phymana | hybmana
					;

fragment manacolor	: 	('W'|'w'|'U'|'u'|'B'|'b'|'R'|'r'|'G'|'g')
					;

fragment phymana	:	'(' manacolor '/p)'
					;

fragment hybmana	:	'(' ('2'|manacolor) '/' manacolor ')'
					;

fragment TEXT		:	(LETTER | APOSTROPHE | SP | COMMA | POINT)+
					;

fragment NAME 		:	(LETTER | APOSTROPHE | SP)+
					;

fragment LETTER		:	('a'..'z'|'A'..'Z')
					;

fragment DIGIT		:	'0'..'9'
					;

fragment NEWLINE	:	'\r'? '\n'
					;

fragment SP 		:	' '
					;

fragment COMMA		:	','
					;

fragment POINT		:	'.'
					;

fragment DASH		:	'--'
					;

fragment APOSTROPHE	:	'\''
					;