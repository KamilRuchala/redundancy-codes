import sys
sys.path.insert(0, '/home/kamil/pytek/JPO/CRC')
sys.path.insert(0, '/home/kamil/pytek/JPO/Hamming')
sys.path.insert(0, '/home/kamil/pytek/JPO/2z5')
sys.path.insert(0, '/home/kamil/pytek/JPO/operacje')
from PyQt4 import QtCore, QtGui
from CRCencoders import *
from koderHamming import *
from twofive import *


from okno import Ui_MainWindow
class StartQT4(QtGui.QMainWindow):
	info="" # informacja potrzebna zaznaczania bitow kolorami
	dzielnik="" # globalny dzielnik potrzebny to przesylania wartosci do usrCrc
	wektorb="" # potrzebny do zapamietania wb
	pozycjaBledu=None
	######################################## Zakladka kodowania CRC ######################################
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		# nazwa klasy
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.hammingInput.setFocus()
	 	QtCore.QObject.connect(self.ui.pushCode,QtCore.SIGNAL("clicked()"), self.kodowanie)
		QtCore.QObject.connect(self.ui.clearOut,QtCore.SIGNAL("clicked()"), self.clear)
		QtCore.QObject.connect(self.ui.pushGenerate,QtCore.SIGNAL("clicked()"), self.gen) # przycisk do gen. losowego
		QtCore.QObject.connect(self.ui.pushOwn,QtCore.SIGNAL("clicked()"), self.wlasny) # przycisk do wprowadzenia dzielnika

		QtCore.QObject.connect(self.ui.encodeButton,QtCore.SIGNAL("clicked()"), self.kodujHammingiem)
		QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"), self.generatorHam)
		QtCore.QObject.connect(self.ui.errorButton,QtCore.SIGNAL("clicked()"), self.errorHam)
		QtCore.QObject.connect(self.ui.clearOutHam,QtCore.SIGNAL("clicked()"), self.clearHam)
		QtCore.QObject.connect(self.ui.detekcjaButton,QtCore.SIGNAL("clicked()"), self.detekcjaHam)
		QtCore.QObject.connect(self.ui.korekcjaButton,QtCore.SIGNAL("clicked()"), self.korekcjaHam)
		
		QtCore.QObject.connect(self.ui.encode2z5,QtCore.SIGNAL("clicked()"), self.koduj2z5)
		QtCore.QObject.connect(self.ui.kodPaskowy,QtCore.SIGNAL("clicked()"), self.rysujKod)
		QtCore.QObject.connect(self.ui.losowo2z5,QtCore.SIGNAL("clicked()"), self.losuj2z5)
		QtCore.QObject.connect(self.ui.czyscOutput,QtCore.SIGNAL("clicked()"), self.clear2z5)
	
	def kodowanie(self):
		informacja=str(self.ui.lineEdit.text())
		if self.blad(informacja)==0: # jesli tego if'a nie bedzie to funkcja zakoduje mimo bledu
			return
		crc8=Crc8(informacja)
		crc10=Crc10(informacja)
		crc12=Crc12(informacja)
		crc16=Crc16(informacja)
		crcXmod=Xmodem16(informacja)
		crcItt=Ccitt16(informacja)
		crc32=Crc32(informacja)
		
		self.ui.crc_8.setText(crc8.kod)
		self.ui.crc_10.setText(crc10.kod)
		self.ui.crc_12.setText(crc12.kod)
		self.ui.crc_16.setText(crc16.kod)
		self.ui.xmodem.setText(crcXmod.kod)
		self.ui.ccitt.setText(crcItt.kod)
		self.ui.crc_32.setText(crc32.kod)
		# sekcja dla usrCrc
		crcU=UserCrc(informacja,self.dzielnik)
		self.ui.user_crc.setText(crcU.kod)
		
	def clear(self):
		self.ui.crc_8.setText("")
		self.ui.crc_10.setText("")
		self.ui.crc_12.setText("")
		self.ui.crc_16.setText("")
		self.ui.xmodem.setText("")
		self.ui.ccitt.setText("")
		self.ui.crc_32.setText("")
		self.ui.user_crc.setText("")
	def gen(self):	
		from gen_ui import Ui_Form
		oknogen = QtGui.QWidget()
		oknogen.ui = Ui_Form()
		oknogen.ui.setupUi(oknogen)
		oknogen.show()
		
		def hand(): #obrazuje zmiane wartosci na suwaku
			wartosc=oknogen.ui.suwak.value()
       			oknogen.ui.ile.setText(str(wartosc))
	        QtCore.QObject.connect(oknogen.ui.suwak,QtCore.SIGNAL("valueChanged(int)"), hand)
		
		def genera():
			a=oknogen.ui.suwak.value()
			from los import losuj
			losowy=losuj(a)
			self.ui.lineEdit.setText(losowy)
		QtCore.QObject.connect(oknogen.ui.pushOk,QtCore.SIGNAL("clicked()"), genera)
		
		#sys.exit(oknogen.exec_())
		
	def wlasny(self):
		from wprowadz_dzielnik import Ui_oknoDzielnik
		okienkoD = QtGui.QWidget() # okno dzielnika
		okienkoD.ui = Ui_oknoDzielnik()
		okienkoD.ui.setupUi(okienkoD)
		okienkoD.show()
		okienkoD.ui.dzielnikInput.setFocus()
		okienkoD.ui.dzielnikInput.setText(self.dzielnik)

		def ok():
			self.dzielnik=str(okienkoD.ui.dzielnikInput.text())	
			if self.blad(self.dzielnik)==0: # musi returnowac bo pomimo bledu wprowadzi ciag
				return
			else:
				okienkoD.close()
		QtCore.QObject.connect(okienkoD.ui.okButton,QtCore.SIGNAL("clicked()"), ok)
	
	def blad(self,st):
		for i in st: #poprawnosc wejscia
			if i !="1" and i !="0":
				message = QtGui.QMessageBox(self)
				message.setText('Zly format danych')
				message.setWindowTitle('Blad')
				message.exec_()
				return 0
	##############################################################################

######################################## Zakladka Hamminga ######################################
		
					
	def kodujHammingiem(self):
		self.info=str(self.ui.hammingInput.text())
		if self.blad(self.info)==0: # jesli tego if'a nie bedzie to funkcja zakoduje mimo bledu
			return
		hamming=HammingEncoder(self.info)
		rozmiar=len(hamming.kod)-len(hamming.info)# liczba bitow parzystosci
		self.ui.kodHamminga.setText(hamming.kod)
		fonttemplate = QtCore.QString("<font color='#9999FF'><b>%1</b></font><font color='black'>%2</font>")
		self.ui.kodHamminga.setText(fonttemplate.arg(hamming.kod[0:rozmiar],hamming.kod[rozmiar:] ))
		
		
	def generatorHam(self):
		from gen_ui import Ui_Form
		oknogen = QtGui.QWidget()
		oknogen.ui = Ui_Form()
		oknogen.ui.setupUi(oknogen)
		oknogen.show()
		
		def hand(): #obrazuje zmiane wartosci na suwaku
			wartosc=oknogen.ui.suwak.value()
       			oknogen.ui.ile.setText(str(wartosc))
	        QtCore.QObject.connect(oknogen.ui.suwak,QtCore.SIGNAL("valueChanged(int)"), hand)
		
		def genera():
			a=oknogen.ui.suwak.value()
			from los import losuj
			losowy=losuj(a)
			self.ui.hammingInput.setText(losowy)
		QtCore.QObject.connect(oknogen.ui.pushOk,QtCore.SIGNAL("clicked()"), genera)

	def errorHam(self):
		from wprowadz_dzielnik import Ui_oknoDzielnik # to okno moze sluzyc rowniez do wektora bledu
		oknoWB = QtGui.QWidget() # okno wektora bledu
		oknoWB.ui = Ui_oknoDzielnik()
		oknoWB.ui.setupUi(oknoWB)
		oknoWB.setWindowTitle('Wektor bledu')
		oknoWB.show()
		oknoWB.ui.dzielnikInput.setFocus()
		oknoWB.ui.dzielnikInput.setText(self.wektorb)

		def ok():
			from wektor_bledu import wektorBlad
			self.wektorb=str(oknoWB.ui.dzielnikInput.text())	
			if self.blad(self.wektorb)==0: 
				return
			else:
				kodzik=str(self.ui.kodHamminga.toPlainText())
				zmienony_kod=""
				if wektorBlad(kodzik,self.wektorb) == "blad" or kodzik=="":
					message = QtGui.QMessageBox(self)
					message.setText('Podano za dlugi wektor lub nie zakodowano informacji')
					message.setWindowTitle('Blad')
					message.exec_()
					return 0
				else:
					(self.wektorb,zmieniony_kod)=wektorBlad(kodzik,self.wektorb)
					self.ui.WektorBledu.setText(self.wektorb)
					self.ui.HammingWithError.setText(zmieniony_kod)

					oknoWB.close()
			
		QtCore.QObject.connect(oknoWB.ui.okButton,QtCore.SIGNAL("clicked()"), ok)
	
	def clearHam(self):
		self.ui.kodHamminga.setText("")
		self.ui.WektorBledu.setText("")
		self.ui.HammingWithError.setText("")
		self.ui.DetekcjaB.setText("")
		self.ui.Skorygowany.setText("")
	
	def detekcjaHam(self):
		from det_kor import zliczacz
		if str(self.ui.WektorBledu.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie podano bledu')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		if zliczacz(self.ui.WektorBledu.toPlainText())=="blad":
			mess = QtGui.QMessageBox(self)
			mess.setText('Detekcja niemozliwa(podano zbyt wiele bledow)')
			mess.setWindowTitle('Blad')
			mess.exec_()
			return 0
		from macierze import defaultMatrix
		(G,H)=defaultMatrix(str(self.ui.hammingInput.text()))
		from det_kor import detekcja
		self.pozycjaBledu=detekcja(str(self.ui.HammingWithError.toPlainText()),G,H)
		kod_blad=self.ui.HammingWithError.toPlainText()
		fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#FF9999'><b>%2</b></font><font color='black'>%3</font>")
		self.ui.DetekcjaB.setText(fonttemplate.arg(kod_blad[0:self.pozycjaBledu],kod_blad[self.pozycjaBledu],kod_blad[self.pozycjaBledu+1:] ))
	
	def korekcjaHam(self):
		if str(self.ui.DetekcjaB.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie wykonano detekcji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from det_kor import korekcja
		self.ui.Skorygowany.setText(korekcja(str(self.ui.HammingWithError.toPlainText()),self.pozycjaBledu))
		tmp=self.ui.Skorygowany.toPlainText()
		fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#B2FF66'><b>%2</b></font><font color='black'>%3</font>")
		self.ui.Skorygowany.setText(fonttemplate.arg( tmp[0:self.pozycjaBledu],tmp[self.pozycjaBledu],tmp[self.pozycjaBledu+1:] ))
###############################                      ##################################

##################################### kod 2z5 ####################################################
	
	def koduj2z5(self):
		a=self.ui.input2z5.text()
		for i in a:
			if i =="0" or i =="1" or i =="2" or i =="3" or i =="4" or i =="5" or i =="6" or i =="7" or i =="8" or i =="9":
				continue
			else:
				message = QtGui.QMessageBox(self)
				message.setText('Zly format wejscia')
				message.setWindowTitle('Blad')
				message.exec_()
				return
		dwa=TwoFive(a)
		self.ui.kod2z5.setText(dwa.standard_kod)
		self.ui.przeplatany2z5.setText(dwa.przeplatany)
	def rysujKod(self):
		st=self.ui.przeplatany2z5.toPlainText()
		if len(self.ui.input2z5.text()) > 40:
			message = QtGui.QMessageBox(self)
			message.setText('Za dlugi input(kod kreskowy obslugiwany do 40 znakow)')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		if self.ui.przeplatany2z5.toPlainText() =="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie zakodowano zadnej informacji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0

		ex = Example(st)
    		ex.show()
		def ok():
			ex.close()
		QtCore.QObject.connect(ex.zam,QtCore.SIGNAL("clicked()"), ok)

	def losuj2z5(self):
		from gen_ui import Ui_Form
		oknogen = QtGui.QWidget()
		oknogen.ui = Ui_Form()
		oknogen.ui.setupUi(oknogen)
		oknogen.show()
		
		def hand(): #obrazuje zmiane wartosci na suwaku
			wartosc=oknogen.ui.suwak.value()
       			oknogen.ui.ile.setText(str(wartosc))
	        QtCore.QObject.connect(oknogen.ui.suwak,QtCore.SIGNAL("valueChanged(int)"), hand)
		
		def genera():
			a=oknogen.ui.suwak.value()
			from los import losujd
			losowy=losujd(a)
			self.ui.input2z5.setText(losowy)
		QtCore.QObject.connect(oknogen.ui.pushOk,QtCore.SIGNAL("clicked()"), genera)
	def clear2z5(self):
		self.ui.kod2z5.setText("")
		self.ui.przeplatany2z5.setText("")
		self.ui.user_crc.setText("")
	def closeEvent(self,event): #zamyka wszystkie "podOkna	
		pass


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
   	myapp = StartQT4()
   	myapp.show()
   	sys.exit(app.exec_())



