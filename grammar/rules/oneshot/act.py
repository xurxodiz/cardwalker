from ...functions.xml.deff import *

def nextquantity(s,l,t):
	return wrap("next", t[2])

def damage(s,l,t):
	return wrap("damage", t[0])

def combatdamage(s,l,t):
	combat = emptytag("combat")
	return wrap("damage", [combat,t[1]])

def noncombatdamage(s,l,t):
	noncombat = emptytag("noncombat")
	return wrap("damage", [noncombat,t[1]])

def thisturn(s,l,t):
	return wrap("turn", emptytag("this"))

def where(s,l,t):
	return wrap("defx", wrap("number", t[0]))

def equal(s,l,t):
	return wrap("equal", wrap("number", t[0]))

def for_(s,l,t):
	return wrap("for", t[1])

def undercontrol(s,l,t):
	return wrap("control", t[1])

def destroy(s,l,t):
	return wrap("destroy", t[1])

def cantregenerate(s,l,t):
	return wrap("cant", emptytag("regenerate"))

def exile(s,l,t):
	if 4 == len(t):
		fromwhere = t[3]
		details = [t[1], fromwhere]
	else:
		details = t[1]
	return wrap("exile", details)

def gainlife(s,l,t):
	return wrap("gain", wrap("life", t[1]))

def tap(s,l,t):
	return wrap("tap", t[1])

def untap(s,l,t):
	return wrap("untap", t[1])

def draw(s,l,t):
	return wrap("draw", t[1])

def discard(s,l,t):
	if 3 == len(t):
		atrandom = emptytag("random")
		what = [atrandom, t[1]] 
	else:
		what = t[1]
	return wrap("discard", what)

def loselife(s,l,t):
	return wrap("lose", wrap("life", t[1]))

def dealquantitydamage(s,l,t):
	details = [t[1], t[4]]
	return wrap("deal", details)

def dealdamage(s,l,t):
	return wrap("deal", t[3])

def sacrifice(s,l,t):
	return wrap("sacrifice", t[1])

def regenerate(s,l,t):
	return wrap("regenerate", t[1])

def putcounter(s,l,t):
	counter = wrap("counter", t[1:2])
	obj = t[5]
	return wrap("put", [counter, obj])

def tokens(s,l,t):
	return wrap("token", t)

def puttoken(s,l,t):
	return wrap("puttoken", t)

def return_(s,l,t):
	return wrap("return", t)

def become(s,l,t):
	return wrap("become", t[1])

def bereduced(s,l,t):
	return wrap("decreaseby", t[3])

def paylife(s,l,t):
	return wrap("pay", wrap("life", t[1]))

def prevention(s,l,t):
	return wrap("prevention", t)

def addmana(s,l,t):
	who = wrap("who", t[4])
	howmuch = t[1]
	return wrap("addmana", [howmuch, who])

def counterspell(s,l,t):
	return wrap("counterspell", t[1])

def effect(s,l,t):
	if 2 == len(t):
		details = t[0:1]
	else:
		details = t[0]
	return wrap("effect", details)

def oneshot(s,l,t):
	return wrap("oneshot", t)