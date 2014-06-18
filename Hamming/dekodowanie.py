import numpy


def dekoduj(kod):
	bit_kontrolny_index=1
	size =len(kod)
	kod.append(8) # kontrolka potrzebna do zakonczenia petli
	while True:
		
		kod[bit_kontrolny_index-1]=2
		bit_kontrolny_index=bit_kontrolny_index*2 
		if bit_kontrolny_index > size:
			break	
	size =len(kod)
	for i in xrange(size):
		if kod[i]==2:
			del kod[i]
		elif kod[i]==8:
			del kod[i]
			break
	del kod[0]
	return kod
