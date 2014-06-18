#http://zylla.wipos.p.lodz.pl/ut/barcode/inter2o5.html 
#http://barcode-coder.com/en/standard-2-of-5-specification-103.html

import sys
sys.path.insert(0, '/home/kamil/pytek/JPO')

from koder import koder
from PyQt4 import QtGui, QtCore
from twofive import *

class TwoFive(koder):
	li = ["00110", "10001", "01001", "11000", "00101","10100","01100","00011","10010","01010"] # lista kodow odpowiadajacym cyfra dziesietnym
	listandard = ["10101110111010", "11101010101110", "10111010101110", "11101110101010", "10101110101110","11101011101010","10111011101010","10101011101110","11101010111010","10111010111010"]
	przeplatany=""
	standard_kod=""
	lista=[] # przyda sie przy przeplataniu
	def __init__(self,informacja):
		self.info=informacja
		self.kod=""
		self.opis="zastosowano koder 2z5"
		self.koduj()
		self.przeplataj()
	def koduj(self):
		for i in self.info:
			if i=="0":
				self.kod=self.kod+self.li[0]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[0])
			if i=="1":
				self.kod=self.kod+self.li[1]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[1])
			if i=="2":
				self.kod=self.kod+self.li[2]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[2])
			if i=="3":
				self.kod=self.kod+self.li[3]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[3])
			if i=="4":
				self.kod=self.kod+self.li[4]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[4])
			if i=="5":
				self.kod=self.kod+self.li[5]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[5])
			if i=="6":
				self.kod=self.kod+self.li[6]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[6])
			if i=="7":
				self.kod=self.kod+self.li[7]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[7])
			if i=="8":
				self.kod=self.kod+self.li[8]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[8])
			if i=="9":
				self.kod=self.kod+self.li[9]
				self.standard_kod=self.standard_kod+self.listandard[int(i)]
				self.lista.append(self.li[9])
	def przeplataj(self):
		if len(self.lista)%2!=0:
			self.lista.insert(0, "00110")
		for i in xrange(len(self.lista)):
			if i%2!=0:
				for x in xrange(5):
					self.przeplatany=self.przeplatany+self.lista[i-1][x]+self.lista[i][x]
		del self.lista[:]

class Pasek:
	dlugosc=80 # przy umiejscawianiu grubego trzeba odjac 2 z dolu i gory bo pogrubia rowniez w gore i w dol 
	gruby=6  
	cienki=2
	peng = QtGui.QPen(QtCore.Qt.red, 0, QtCore.Qt.SolidLine)
	penc = QtGui.QPen(QtCore.Qt.red, 0, QtCore.Qt.SolidLine)
	def rysuj_gruby(self):
		pass
	def rysuj_cienki(self):
		pass

class Pasek_bialy(Pasek):
	def __init__(self):
		self.peng = QtGui.QPen(QtCore.Qt.white, 6, QtCore.Qt.SolidLine)
		self.penc = QtGui.QPen(QtCore.Qt.white, 2, QtCore.Qt.SolidLine)
	def rysuj_gruby(self,x1,y1,qp):
		qp.setPen(self.peng)
        	qp.drawLine(x1, y1+2, x1, y1+self.dlugosc-2)
	def rysuj_cienki(self,x1,y1,qp):
		qp.setPen(self.penc)
        	qp.drawLine(x1, y1, x1, y1+self.dlugosc)	

class Pasek_czarny(Pasek):
	def __init__(self):
		self.peng = QtGui.QPen(QtCore.Qt.black, 6, QtCore.Qt.SolidLine)
		self.penc = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
	def rysuj_gruby(self,x1,y1,qp):
		qp.setPen(self.peng)
        	qp.drawLine(x1, y1+2, x1, y1+self.dlugosc-2)
	def rysuj_cienki(self,x1,y1,qp):
		qp.setPen(self.penc)
        	qp.drawLine(x1, y1, x1, y1+self.dlugosc)


class Kod_kreskowy:
	info=""
	y=0 # na jakiej wysokosci rysujemy
	x=0
	bialy=Pasek_bialy()
	czarny=Pasek_czarny()
        qp= QtGui.QPainter()
	def __init__(self,inf,wsp_x,wsp_y,qp):
		self.info=inf
		self.x=wsp_x
		self.y=wsp_y
		self.qp=qp
	def rysuj_kod(self): 
		licznik=0
		 #rysuje start
		self.czarny.rysuj_cienki(self.x,self.y,self.qp)
		self.x=self.x+2
		self.bialy.rysuj_cienki(self.x,self.y,self.qp)
		self.x=self.x+2
		self.czarny.rysuj_cienki(self.x,self.y,self.qp)
		self.x=self.x+2
		self.bialy.rysuj_cienki(self.x,self.y,self.qp)
		if self.info[0]=="1":
			self.x=self.x+4
		else:
			self.x=self.x+2
		for i in xrange(len(self.info)):
			if i == len(self.info)-1: # chce uniknac indexOutRange, ostatni zawsze bialy
				if self.info[i]=="1":
					self.bialy.rysuj_gruby(self.x,self.y,self.qp)
					self.x=self.x+6
				if self.info[i]=="0":
					self.bialy.rysuj_cienki(self.x,self.y,self.qp)
					self.x=self.x+4
			else: #sprawdzam jaki jest nastepny elemeny by wiedziec o ile pikseli przesuwac
				if self.info[i]=="1" and licznik%2==0 and self.info[i+1]=="0":
					self.czarny.rysuj_gruby(self.x,self.y,self.qp)
					self.x=self.x+4
				if self.info[i]=="1" and licznik%2==0 and self.info[i+1]=="1":
					self.czarny.rysuj_gruby(self.x,self.y,self.qp)
					self.x=self.x+6
				if self.info[i]=="1" and licznik%2!=0 and self.info[i+1]=="0":
					self.bialy.rysuj_gruby(self.x,self.y,self.qp)
					self.x=self.x+4
				if self.info[i]=="1" and licznik%2!=0 and self.info[i+1]=="1":
					self.bialy.rysuj_gruby(self.x,self.y,self.qp)
					self.x=self.x+6
				if self.info[i]=="0" and licznik%2==0 and self.info[i+1]=="0":
					self.czarny.rysuj_cienki(self.x,self.y,self.qp)
					self.x=self.x+2
				if self.info[i]=="0" and licznik%2==0 and self.info[i+1]=="1":
					self.czarny.rysuj_cienki(self.x,self.y,self.qp)
					self.x=self.x+4
				if self.info[i]=="0" and licznik%2!=0 and self.info[i+1]=="0":
					self.bialy.rysuj_cienki(self.x,self.y,self.qp)
					self.x=self.x+2
				if self.info[i]=="0" and licznik%2!=0 and self.info[i+1]=="1":
					self.bialy.rysuj_cienki(self.x,self.y,self.qp)
					self.x=self.x+4
			licznik=licznik+1
		# rysuje stop
		self.czarny.rysuj_gruby(self.x,self.y,self.qp)
		self.x=self.x+4
		self.bialy.rysuj_cienki(self.x,self.y,self.qp)
		self.x=self.x+2
		self.czarny.rysuj_cienki(self.x,self.y,self.qp)

class Example(QtGui.QWidget):
    			ciag=""
    			def __init__(self,a):
        			super(Example, self).__init__()
        			self.initUI()
        			self.ciag=a
    			def initUI(self):      

        			self.setGeometry(300, 300, 400, 150)
        			self.setWindowTitle('Kod paskowy')
				self.zam = QtGui.QPushButton('Zamknij', self)
				self.zam.move(170, 120)
        			self.show()

			def paintEvent(self, e):

        			qp = QtGui.QPainter()
        			qp.begin(self)
        			self.drawLines(qp)
        			qp.end()
        
    			def drawLines(self,qp):
				kodzik=Kod_kreskowy(self.ciag,20,10,qp)
				
				kodzik.rysuj_kod()
				self.setGeometry(300, 300, kodzik.x+20, 150) # resize okna w zaleznosci od dlugosci kodu
				self.zam.move(kodzik.x/2 -15, 120)

