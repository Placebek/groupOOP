# 2- нұсқа
class Road:  
    def __init__(self, name, length): self.name, self.length = name, length  
    def __str__(self): return f"{self.name}, {self.length} km"

class Building:  
    def __init__(self, name, floors): self.name, self.floors = name, floors  
    def __str__(self): return f"{self.name}, {self.floors} floors"

class Park:  
    def __init__(self, name, area): self.name, self.area = name, area  
    def __str__(self): return f"{self.name}, {self.area} ha"

class City:  
    def __init__(self, name): self.name, self.roads, self.buildings, self.parks = name, [], [], []  
    def add(self, obj): getattr(self, obj.__class__.__name__.lower() + 's').append(obj)  
    def show(self):  
        print(f"{self.name}", *self.roads, *self.buildings, *self.parks, sep="\n")  
    def __del__(self): print(f"Deleting {self.name}!")  

city = City("Astana")  
city.add(Road("Main St", 10))  
city.add(Building("Tower", 25))  
city.add(Park("Central", 15))  
city.show()  
del city  
