from abc import ABC, abstractmethod


class University:
	def fit(self):
		print("Darkhan")


class Faculty:
	def __init__(self, name):
		self.university = University()
		self.name = name
		self.faculty_name = []

	def append_faculty(self, name):
		self.faculty_name.append(self.name)
		return self.faculty_name

	def pop_faculty(self):
		if len(self.faculty_name) == 0:
			print("Нет факультетов")
		return self.faculty_name.pop(-1)


faculty = Faculty()


class University(ABC):
	@abstractmethod
	def study(self):
		pass


class Faculty(University):
	def study(self):
		pass


class Dekan(University):
	def study(self):
		pass


class Home(ABC):
	@abstractmethod
	def where(self):
		pass


class Room(Home):
	def where(self):
		pass


class Window(Home):
	def where(self):
		pass
 
