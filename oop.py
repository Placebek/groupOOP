class ZooAnimal:
	def __init__(self, species, weigth, roar):
		self.__species = species
		self.__weigth = weigth
		self.roar = roar


	def get_species(self):
		return self.__species

	def get_weigth(self):
		return self.__weigth
	
	def set_species(self, species):
		self.__species = species

	def set_weigth(self, weigth):
		self.__weigth = weigth

	def animal_roar(self):
		print(self.roar)
	
zooanimal = ZooAnimal("Лев", 120, "arrr")
zooanimal.animal_roar()
print(zooanimal.get_species())
print(zooanimal.get_weigth())

class Lion(ZooAnimal):
	def __init__(self, species, weigth, roar):
		super().__init__(species, weigth, roar)
		

	def animal_roar(self):
		super().animal_roar()

zooanimal = ZooAnimal("Лев", 200, "ar")
zooanimal.animal_roar()
print(zooanimal.get_species())
print(zooanimal.get_weigth())

class Elephant(ZooAnimal):
	def __init__(self, species, weigth, roar,trumpet):
		super().__init__(species, weigth, roar)
		self.trumpet = trumpet

	def animal_roar(self):
		super().animal_roar()

	def info(self):
		return self.trumpet

class Penguin(ZooAnimal):
	def __init__(self, species, weigth, roar, swim):
		super().__init__(species, weigth, roar)
		self.swim = swim

	def animal_roar(self):
		super().animal_roar()

	def info(self):
		return self.swim
