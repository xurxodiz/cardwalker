def concat(lst):
	return "".join(lst)

def wrap(tag, lst):
	return "<%s>%s</%s>" % (tag.lower(), concat(lst), tag.lower())

def emptytag(tag):
	return "<%s />" % tag.lower()

def lowername(dct):
	return dct.keys()[0].lower()