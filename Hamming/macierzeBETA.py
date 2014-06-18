
import numpy # trzeba doinstalowac 

def defaultMatrix(inf): #rozmiar (l.bitow parz x l.bitow zakodowanego slowa

	binarne_info=[]
	for x in inf:
		tmp=int(x)
		binarne_info.append(tmp)

	size=len(binarne_info)
	bit_kontrolny_index=1  # zmienna do przesuwania miejca Bit Ctrl w petli index bitu 
	tab_par1=[] #tablica miejsc bitow parzystosci(zapisuje miejsca bo pozniej beda potrzebne)
	zakodowane=binarne_info
	while True: 
		zakodowane.insert(bit_kontrolny_index-1,"p")
		tab_par.append(bit_kontrolny_index-1) # -1 bo indeksujemy w tablicy od 0
		size = size +1 # wpisalem bit kontr., size rosnie	
		bit_kontrolny_index=bit_kontrolny_index*2
		if bit_kontrolny_index > size:
			break

	####################################### MACIERZ H ###################################
	H=numpy.zeros(shape=(len(tab_par),size)) #rozmiar l.bit.parz. na l.bit.kodu
	count1=0
	count2=0 
	for x in xrange(len(tab_par)):
		count1=0; #liczniki do korzystania z algo. ile opuszczac bitow i co ile wypelniac jedynkami 
		count2=tab_par[x] +1
		for i in xrange(size): # tworzymy macierz parzystosci H
			if i >= tab_par[x]: #uwazamy na indeksy(numerujemy indeksy od zera, a dla algorytmu numery od 1)
				if  count2 == tab_par[x]+1:
					H[x,i]=1
					count1=count1 + 1
					if count1 == tab_par[x]+1:
						count2 =0
				elif count1 == tab_par[x]+1:
					H[x,i]=0 #linijka nie potrzebna bo macierz wyjsciowo ma zera, ale jest dla przejrzystosci :)
					count2=count2 + 1
					if count2 == tab_par[x]+1:
						count1 =0
	Hp=numpy.zeros(shape=(len(tab_par),size))
	wsk=-1
	for i in xrange(len(tab_par)):
		Hp[i,:]=H[wsk,:]
		wsk=wsk-1
	H=Hp
	####################################### MACIERZ G ###################################
	tab_inf_index=[]	
	for i in xrange(len(zakodowane)): # tworze tablice z numerami indeksow(miejsc gdzie znajduja sie informacje)
		if zakodowane[i]=="p":
			continue
		else:
			tab_inf_index.append(i)
	lbinf=len(tab_inf_index) # liczba bitow informacji
	G=numpy.zeros(shape=(lbinf,size)) #rozmiar l.bit.informacji na l.bit.kodu	
	
	H2=numpy.copy(H) # kopia macierzy H do manewrowania kolumnami(doprowadzam do postaci H=A|I)
	wsk=size-len(tab_par)
	wsk2=-1	
	for i in xrange(len(tab_par)):
		tmp=numpy.copy(H2[:,tab_par[wsk2]])
		H2[:,tab_par[wsk2]]=H2[:,wsk]
		H2[:,wsk]=tmp
		wsk=wsk+1
		wsk2=wsk2-1

	A=numpy.copy(H2[:,0:lbinf])	
	At=numpy.zeros(shape=(lbinf,len((tab_par))))	# A transponowana
	
	for x in xrange(lbinf):
		At[x,:]=A[:,x]

	I=jednostkowa(lbinf)
	for x in xrange(lbinf):
		G[:,x]=I[:,x]
	for x in xrange(size-lbinf):
		G[:,x+lbinf]=At[:,x] 
	 
#	wsk=size-len(tab_par)
#	wsk2=-1	
#	for i in xrange(len(tab_par)):
#		tmp=numpy.copy(G[:,tab_par[wsk2]])
#		G[:,tab_par[wsk2]]=G[:,wsk]
#		G[:,wsk]=tmp
#		wsk=wsk+1
#		wsk2=wsk2-1
	return (G,H)

#############################################################################################

def jednostkowa(rozmiar):
	I=numpy.zeros(shape=(rozmiar,rozmiar))
	for x in xrange(rozmiar):
		I[x,x]=1
	return I
