# 1 tapsyrma 

class Animal:
    def __init__(self, name):
        self.name = name 
    def zhanuar(self):
        print(f"Жануар - {self.name}.")
class Zoo:
    def __init__(self, name_zoo):
        self.name_zoo = name_zoo
        self.zoo_animals = []

    def add_animals(self, animal):
        self.zoo_animals.append(animal)

    def count_animals(self):
        print(f"{self.name_zoo} - те жануарлар саны {len(self.zoo_animals)}.")

animal = Animal("Tiger")
animal2 = Animal("Lion")
animal.zhanuar()
animal2.zhanuar()

zoo = Zoo("Zoopark")
zoo.add_animals(animal2)
zoo.add_animals(animal)
zoo.count_animals()

# 2 tapsyrma 
