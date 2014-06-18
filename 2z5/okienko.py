class Example(QtGui.QWidget):
    
    			def __init__(self):
        			super(Example, self).__init__()
        			self.initUI()
        
    			def initUI(self):      

        			self.setGeometry(300, 300, 280, 270)
        			self.setWindowTitle('Pen styles')
				redb = QtGui.QPushButton('Red', self)
				redb.move(10, 10)
        			self.show()

			def paintEvent(self, e):

        			qp = QtGui.QPainter()
        			qp.begin(self)
        			self.drawLines(qp)
        			qp.end()
        
    			def drawLines(self,qp):
				kodzik=Kod_kreskowy("100100101101001010101010",20,10,qp)
				kodzik.rysuj_kod()
