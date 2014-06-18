#http://zylla.wipos.p.lodz.pl/ut/barcode/inter2o5.html 

import sys
from PyQt4 import QtGui, QtCore
from a import *

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
		for i in xrange(len(self.info)):
			if i == len(self.info)-1: # chce uniknac indexOutRange
				if self.info[i]=="1" and licznik%2==0:
					self.czarny.rysuj_gruby(self.x,self.y,self.qp)
				if self.info[i]=="1" and licznik%2!=0:
					self.bialy.rysuj_gruby(self.x,self.y,self.qp)
				if self.info[i]=="0" and licznik%2==0:
					self.czarny.rysuj_cienki(self.x,self.y,self.qp)
				if self.info[i]=="0" and licznik%2!=0:
					self.bialy.rysuj_cienki(self.x,self.y,self.qp)
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


