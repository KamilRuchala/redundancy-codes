import numpy # trzeba doinstalowac 
def xor(tab):
	licznik=0
	for x in tab:
		if x==1:
			licznik = licznik +1
	if licznik % 2 ==0:
		return 0
	else:
		return 1

def encode(info):
	size=len(info) # rozmiar informacji
	for x in info: #sprawdzam czy poprawnie wpisujemy
		if x != "1" and x !="0": 
			print "blad"
			break

	binarne_info=[] # informacja w binarce(raw_input wczytuje string)
	for x in info:
		tmp=int(x)
		tmp=bin(tmp)
		binarne_info.append(tmp)

	bit_kontrolny_index=1  # zmienna do przesuwania miejca Bit Ctrl w petli index bitu 
	zakodowane=[]
	tab_par=[] #tablica miejsc bitow parzystosci(zapisuje miejsca bo pozniej beda potrzebne)
	zakodowane=binarne_info # bedziemy wstawiac miedzy bity informacji bity parzystosci
	while True:
		zakodowane.insert(bit_kontrolny_index-1,2)
		tab_par.append(bit_kontrolny_index-1) 
		size = size +1 # wpisalem bit kontr., size rosnie	
		bit_kontrolny_index=bit_kontrolny_index*2
		if bit_kontrolny_index > size:
			break


	najdluzsze_bity=len(bin(len(zakodowane))) # najwyzsza wartosc indeksu ( licze dlugosc najdluzszej interpretacji binarnej)

	#tu ma byc zliczacz jedynek
	liczba=0
	for x in xrange(len(zakodowane)):
		if zakodowane[x]=='0b1':
			liczba=liczba+1


	tablica_pomocnicza2=numpy.zeros(shape=(liczba,najdluzsze_bity-2)) #minus 2 bo nie uwzgledniam "0b" na poczatku binarnego zapisu
	#tablica ma zawierac: caly wiersz odpowiada kodowi binarnemu pozycji jedynki w kodzie
	przesuwacz_wierszy=0
	for x in xrange(len(zakodowane)): #numery indeksow zawierajacych jedynki || http://edu.i-lo.tarnow.pl/inf/alg/002_struct/0010.php tworze macierz do xor'a
	
		if zakodowane[x]=='0b1':
			tmp=bin(x+1) # x+1 bo przechodze z indeksowania z 0 na od 1
			przesuwacz=len(tmp)-1
			przesuwacz_kolumn=najdluzsze_bity-3
			while tmp[przesuwacz] != 'b':
				tablica_pomocnicza2[przesuwacz_wierszy,przesuwacz_kolumn]=tmp[przesuwacz]
				przesuwacz=przesuwacz-1
				przesuwacz_kolumn=przesuwacz_kolumn-1
			if tmp[przesuwacz] == 'b':
				przesuwacz_wierszy=przesuwacz_wierszy+1

	p=[] #tablica wartosci bitow parzystosci

	for x in xrange(najdluzsze_bity-2):
		tablica_pomocnicza=[] # wpisuje do niej wektor(kolumny macierzy i bd liczyc xor'a)
		for i in xrange(liczba):
			tablica_pomocnicza.append(tablica_pomocnicza2[i,x])
		p.append(xor(tablica_pomocnicza))
	wsk=len(p) -1


	for x in xrange(len(zakodowane)):
		if zakodowane[x] == 2:
			zakodowane[x]= bin(p[wsk])
			wsk=wsk-1

	zakodowane2=[]
	for i in xrange(len(zakodowane)):
		if zakodowane[i]=='0b0':
			zakodowane2.append(0)
		elif zakodowane[i]=='0b1':
			zakodowane2.append(1)	
	return zakodowane2

################################################################################################



