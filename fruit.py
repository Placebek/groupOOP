# 4 нұсқа Төлегенов Бақдәулет ИС-22-2
class Fruit:
    def __init__(self, name: str, taste: int):
        self._name = name
        self._taste = taste

    def set_name(self, name: str):
        self._name = name

    def set_taste(self, taste: int):
        self._taste = taste

    def get_name(self) -> str:
        return self._name

    def get_taste(self) -> int:
        return self._taste
    
class Apple(Fruit):
    def crunch(self):
        return "Алма қытырлақ!"
    
    def fruit_sound(self):
        return self.crunch()
    
class Orange(Fruit):
    def peel(self):
        return "Апельсин тазартылады!"
    
    def fruit_sound(self):
        return self.peel()
    
class Banana(Fruit):
    def peel(self):
        return "Банан тазартылады!"
    
    def fruit_sound(self):
        return self.peel()

if __name__ == "__main__":
    apple = Apple("Алма", 1)
    orange = Orange("Апельсин", 2)
    banana = Banana("Банан", 3)

    fruits = [apple, orange, banana]
    
    for fruit in fruits:
        print(f"{fruit.get_name()} says: {fruit.fruit_sound()}")