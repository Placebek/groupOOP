#5 
#2-тапсырма
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
class AnimalFactory:
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

def get_animal_sound(factory: AnimalFactory):
    animal = factory.create_animal()
    return animal.sound()

print(get_animal_sound(DogFactory()))
print(get_animal_sound(CatFactory()))