class Appliance:
	def __init__(self,brand, power):
		self.__brand = brand
		self.__power = power
	
	def get_brand(self):
		return self.__brand
	def get_power(self):
		return self.__power
	def set_brand(self, brand):
		self.__brand = brand
	def set_power(self, power):
		self.__power = power

class WashingMachine(Appliance):
	def __init__(self,brand, power):
		self.__brand = brand
		self.__power = power
	def wash(self):
		print("Стиральная машина стирает")
	def operate(self):
		print("BRRRR")
	
class Refrigerator(Appliance):
	def __init__(self,brand, power):
		self.__brand = brand
		self.__power = power
	def cool(self):
		print("Holodilnik ohlozhdaet")
	#@overriding
	def operate(self):
		print("Bzzzz")
class Microwave(Appliance):
	def __init__(self,brand, power):
		self.__brand = brand
		self.__power = power
	def heat(self):
		print("Microvalnovka razogrevaet")
	#@overriding
	def operate(self):
		print("wwwwww")
		
ap = Appliance(5,10)

print(ap.get_brand())
print(ap.get_power())

WM = WashingMachine(1,10)

WM.wash()
WM.operate()

RG = Refrigerator(1,10)
RG.cool()
RG.operate()

MC = Microwave(1,10)
MC.heat()
MC.operate()