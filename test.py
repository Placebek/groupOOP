#3 Nuska
class Singleton:
    _instacne = None
    def __new__(cls, *args, **kwargs):
        if cls._instacne is None:
            cls._instacne = super().__new__(cls)
        return cls._instacne

s1 = Singleton()
s2 = Singleton()
print(s1 == s2)



class Player:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self):
        self.list = []
        self.age = []
        
    def adder(self, name, age):
        self.list.append(name)
        self.age.append(age)
    
    def deleter(self, name, age):
        self.list.pop(name)
        self.listage.pop(age)
    
    def calc(self):
        sum = 0
        a = len(self.age)
        for i in range(a):
            sum = sum + self.age[i]
        return sum / a

p1 = Player("Nurkeldi")
p2 = Player("Nur")        

team = Team()
team.adder(p1,18)
team.adder(p2,19)

print(team.calc())
