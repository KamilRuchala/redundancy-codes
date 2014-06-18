import sys
sys.path.insert(0, '/home/kamil/pytek/JPO')

def xor(x1,x2):
	tab=""
	tab=tab+x1
	tab=tab+x2
	licznik=0
	for x in tab:
		if x=='1':
			licznik = licznik +1
	if licznik % 2 ==0:
		return "0"
	else:
		return "1"

from koder import koder

class koderCRC(koder):
	n=0 #ilu bitowy koder crc
	dzielnik=0
	tmp="" # string na iformacje + zera
	def __init__(self):
		self.info="None"
		self.kod="None"
		self.opis="zastosowano koder CRC"
	def setN(self,a):
		self.n=a
	def prepare(self):
		self.tmp=self.info # informacja + zerowe bity(dodane w nastepujacej petli)	
		for x in xrange(self.n):
			self.tmp=self.tmp+"0"
	def koduj(self):
		self.prepare()
		if self.dzielnik == "": # tylko dla usrCrc
			return
		while True:
			tmp2="" # zmienna pomocnicza
			for i in xrange(len(self.tmp)): #usuwam 0 z poczatku( operacje xor wykonuje sie po napotkaniu 1)
				if self.tmp[i]=="0":
					continue
				else: 
					tmp2=self.tmp[i:]
					break
			
			tmp3=tmp2 # do wpisywania bitow
			
			if len(tmp2)>=self.n+1:
				list1=list(tmp3)
				for x in xrange(self.n+1):
					list1[x]=xor(tmp2[x],self.dzielnik[x])
				tmp3=''.join(list1)
			else:
				break
			self.tmp=tmp3
		
		self.kod=self.tmp[len(self.tmp)-self.n:]


