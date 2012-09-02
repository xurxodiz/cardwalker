#! /usr/bin/env python

import sys
import antlr3
import antlr3.tree
from gr.CardLexer import CardLexer
from gr.CardParser import CardParser
#from gr.CardWalker import CardWalker

path = "oracle/card.txt"

char_stream = antlr3.ANTLRFileStream(path, 'utf8')
lexer = CardLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = CardParser(tokens)
r = parser.card()

"""
# this is the root of the AST
root = r.tree

nodes = antlr3.tree.CommonTreeNodeStream(root)
nodes.setTokenStream(tokens)
ev = CardWalker(nodes)
ev.card()
"""