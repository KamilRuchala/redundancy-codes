from wektor_bledu import blad
from kodowanie2 import koder
from kodowanie2 import dekoder
from kodowanie import koduj
from det_kor import *
from macierze import defaultMatrix
from operacje import stringer
#from wszystko import defaultMatrix


info=raw_input("podaj ciag: ")
(G,H)=defaultMatrix(info)
blada=raw_input("wprowadz blad: ")
kod=koder(info)
print stringer(kod)
kodb=blad(kod,blada)
print stringer(kodb)
a=detekcja(inter(stringer(kodb)),G,H)
print a
c=korekcja(kodb,a)
print c
inf=dekoder(kodb)
print G
print inf
print H


