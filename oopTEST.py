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

F = Fruit("Apple", 'Sweet') 

print(F.get_name())  
