natijalar = [] # empty list

class Mashina():
	def __init__ (self,nomi: str,narxi: int):
		self.nomi= nomi
		self.narxi = narxi
		print(f"{nomi} ning narxi hozirda {narxi} dollar")
		natijalar.append(self)
	def __repr__ (self):   # __repr__ defoult holatdan qayta uqish uchun
		return f"{self.nomi}, {self.narxi}"


Mashina("tesla",20000)
Mashina("BMW",20000000)
Mashina("mers",3450000)
Mashina("porsche",245670000)

print(natijalar)  # har bir chaqirilgan class malumoti empty listga saqlanib borgandi 
#output:
'''tesla ning narxi hozirda 20000 dollar
BMW ning narxi hozirda 20000000 dollar
mers ning narxi hozirda 3450000 dollar
porsche ning narxi hozirda 245670000 dollar
[tesla, 20000, BMW, 20000000, mers, 3450000, porsche, 245670000]
[Finished in 42ms]'''