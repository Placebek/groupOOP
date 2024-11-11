class Appliance:
    def __init__(self, brand, power):
        self.__brand = brand   
        self.__power = power   
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand
    
    def get_power(self):
        return self.__power
    
    def set_power(self, power):
        self.__power = power

A = Appliance("Louis Vuitton", "bag")

print(A.get_brand())  
print(A.get_power())  
