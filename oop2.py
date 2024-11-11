class Person:
	def start_heart(self):
		return "Соғады"
	
	def start_brain(self):
		return "Жұмыс істеп тұр"


class Heart:
	def __init__(self):
		self.heart = Person()
		self.brain = Person()
	
	def start_heart(self):
		return heart.start_heart()
	
	def start_brain(self):
		return brain.start_brain()


heart = Heart()
print(heart.start_heart())


class Person:
	def __init__(self, brain, heart):
		self.brain = brain
		self.heart = heart


class Students:
	def __init__(self, organism):
		self.organism = Person()
	


class Darkhan:
	def __init__(self, jurek):
		self.organism.heart = jurek

	def start(self):
		return self.organism.heart
		
class Nurgeldi:
	def __init__(self, mi):
		self.organism.brain = mi
	
	def start(self):
		return self.organism.brain

darkhan = Darkhan()
nurgeldi = Nurgeldi()

  


	