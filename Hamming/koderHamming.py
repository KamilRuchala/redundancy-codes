import sys
sys.path.insert(0, '/home/kamil/pytek/JPO')

from koder import koder
from kodowanie2 import *

class HammingEncoder(koder):
	def __init__(self,informacja):
		self.info=informacja
		self.kod="None"
		self.opis="zastosowano koder Hamminga"
		self.koduj()
	def koduj(self):
		self.kod=encoder(self.info)


