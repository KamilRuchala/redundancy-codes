
import numpy # trzeba doinstalowac 

def defaultMatrix(inf): #rozmiar (l.bitow parz x l.bitow zakodowanego slowa
	binarne_info=[]
	for x in inf:
		tmp=int(x)
		binarne_info.append(tmp)

	size=len(binarne_info)
	bit_kontrolny_index=1  # zmienna do przesuwania miejca Bit Ctrl w petli index bitu 
	tab_par=[] #tablica miejsc bitow parzystosci
	zakodowane=binarne_info
	while True: 
		zakodowane.insert(bit_kontrolny_index-1,"p")
		tab_par.append(bit_kontrolny_index-1) # -1 bo indeksujemy w tablicy od 0
		size = size +1 # wpisalem bit kontr., size rosnie	
		bit_kontrolny_index=bit_kontrolny_index*2
		if bit_kontrolny_index > size:
			break
	tab_inf=[]
	for i in xrange(len(zakodowane)):
		if zakodowane[i] != "p":
			tab_inf.append(i)

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
#	Hp=numpy.zeros(shape=(len(tab_par),size))
#	wsk=-1
#	for i in xrange(len(tab_par)):
#		Hp[i,:]=H[wsk,:]
#		wsk=wsk-1
#	H=Hp
	####################################### MACIERZ G ###################################
	tab_inf_index=[]	
	for i in xrange(len(zakodowane)): # tworze tablice z numerami indeksow(miejsc gdzie znajduja sie informacje)
		if zakodowane[i]=="p":
			continue
		else:
			tab_inf_index.append(i)
	lbinf=len(tab_inf_index) # liczba bitow informacji
	G=numpy.zeros(shape=(size,lbinf)) #rozmiar l.bit.informacji na l.bit.kodu	
	
	H2=numpy.copy(H) # kopia macierzy H do manewrowania kolumnami(doprowadzam do postaci H=I|A)
	wsk=0	
	for i in tab_par:
		tmp=numpy.copy(H2[:,i])
		H2[:,i]=H2[:,wsk]
		H2[:,wsk]=tmp
		wsk=wsk+1
	

	A=numpy.copy(H2[:,len(tab_par):])	

	lbpar=len(tab_par)
	I=jednostkowa(lbinf)
	for x in xrange(lbpar):
		G[x,:]=A[x,:] 
	for x in xrange(lbinf):
		G[x+lbpar,:]=I[x,:]

	 
	wsk=lbpar # sprawa jest taka. wiersze macierzy jednostkowej znajduja sie na miejscach bitow informacji	
#	for i in tab_inf:
#		tmp=numpy.copy(G[i,:])
#		G[i,:]=G[wsk,:]
#		G[wsk,:]=tmp
#		wsk=wsk+1
	
	Gt=numpy.zeros(shape=(lbinf,size))	# G transponowana
	for x in xrange(lbinf):
		Gt[x,:]=G[:,x]
	return (Gt,H2)

#############################################################################################

def jednostkowa(rozmiar):
	I=numpy.zeros(shape=(rozmiar,rozmiar))
	for x in xrange(rozmiar):
		I[x,x]=1
	return I
