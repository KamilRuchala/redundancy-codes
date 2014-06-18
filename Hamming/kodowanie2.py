
import numpy
from macierze import defaultMatrix
from macierze import jednostkowa
from operacje import *


sizeinf=0
sizepar=0

def encoder(inf):
	global sizeinf
	sizeinf=len(inf)
	

	(G,H)=defaultMatrix(inf)
	global sizepar
	sizepar=len(H)
	c=mnozenie(G,inf)
	kod=[]
	tmp=[]
	for x in xrange(len(H[1])):
		tmp=c[:,x]
		kod.append(suma(tmp))
	return stringer(kod)	

def dekoder(kod):
	info=[]
	for x in xrange(sizeinf):
		info.append(kod[x+sizepar])
	return stringer(info)
	

