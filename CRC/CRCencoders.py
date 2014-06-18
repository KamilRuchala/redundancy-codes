#http://ghsi.de/CRC/index.php?Polynom=1100000001111&Message=15 zgodnie z tym dziala
#http://depa.usst.edu.cn/chenjq/www2/software/crc/CRC_Javascript/CRCcalculation.htm
from koderCRC import koderCRC

class Crc8(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-8"
		self.n=8
		self.dzielnik="100000111"
		self.koduj()

class Crc10(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-10"
		self.n=10
		self.dzielnik="11000110011"
		self.koduj()

class Crc12(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-12"
		self.n=12
		self.dzielnik="1100000001111"
		self.koduj()

class Crc16(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-16"
		self.n=16
		self.dzielnik="11000000000000101"
		self.koduj()

class Xmodem16(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-16"
		self.n=16
		self.dzielnik="11000010000001000"
		self.koduj()

class Ccitt16(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-16"
		self.n=16
		self.dzielnik="10001000000100001"
		self.koduj()

class Crc32(koderCRC):
	def __init__(self,i):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-16"
		self.n=32
		self.dzielnik="100000100110000010001110110110111"
		self.koduj()

class UserCrc(koderCRC):
	def __init__(self,i,dziel):
		self.info=i
		self.kod="None"
		self.opis="zastosowano koder CRC-16"
		self.n=len(dziel)-1
		self.dzielnik=dziel
		if self.dzielnik != "":
			self.koduj()



	
