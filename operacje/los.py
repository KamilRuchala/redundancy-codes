def losuj(dlg):
	from random import randint
	ciag=""
	for i in xrange(dlg):
		ciag=ciag+str(randint(0,1))
	return ciag

def losujd(dlg):
	from random import randint
	ciag=""
	for i in xrange(dlg):
		ciag=ciag+str(randint(0,9))
	return ciag

