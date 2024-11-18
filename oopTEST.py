# 4 - нұсқа
class Fruit:
    def __init__(self, name, taste):
        self.__name = name  
        self.__taste = taste  
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_taste(self):
        return self.__taste
    
    def set_taste(self, taste):
        self.__taste = taste
    
    def describe(self):
        return "Это настоящий фрукт"

class Apple(Fruit):
    def __init__(self):
        super().__init__("Apple", "Crunchy")
    
    def crunch(self):
        return "Яблоко начинает хрустеть!"
    
    def describe(self):
        return "Это яблоко"

class Orange(Fruit):
    def __init__(self):
        super().__init__("Orange", "Citrusy")
    
    def peel(self):
        return "Апельсин очищается от кожуры"
    
    def describe(self):
        return "Это апельсин"

class Banana(Fruit):
    def __init__(self):
        super().__init__("Banana", "Soft")
    
    def peel(self):
        return "Банан очищается от кожуры"
    
    def describe(self):
        return "Это банан"

fruits = [Apple(), Orange(), Banana()]

for fruit in fruits:
    print(fruit.describe())
    if isinstance(fruit, Apple):
        print(fruit.crunch())
    if isinstance(fruit, Orange) or isinstance(fruit, Banana):
        print(fruit.peel())
