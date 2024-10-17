# 3 - нұсқа
class Appliance:
    def _init_(self, brand, power):
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
    
    def operate(self):
        return "Рабочий прибор"

class WashingMachine(Appliance):
    def _init_(self, brand, power):
        super()._init_(brand, power)
    
    def wash(self):
        return "Стиральная машина стирает одежду."
    
    def operate(self):
        return "Стиральная машина в рабочем состоянии"

class Refrigerator(Appliance):
    def _init_(self, brand, power):
        super()._init_(brand, power)
    
    def cool(self):
        return "Холодильник охлаждается."
    
    def operate(self):
        return "Холодильник в рабочем состоянии"

class Microwave(Appliance):
    def _init_(self, brand, power):
        super()._init_(brand, power)
    
    def heat(self):
        return "Микроволновая печь разогревает пищу."
    
    def operate(self):
        return "Микроволновая печь в рабочем состоянии"

appliances = [
    WashingMachine("LG", "1500W"),
    Refrigerator("Samsung", "800W"),
    Microwave("Panasonic", "1200W")
]

for appliance in appliances:
    print(f"Brand: {appliance.get_brand()}, Power: {appliance.get_power()}")
    print(appliance.operate())
    
    if isinstance(appliance, WashingMachine):
        print(appliance.wash())
    elif isinstance(appliance, Refrigerator):
        print(appliance.cool())
    elif isinstance(appliance, Microwave):
        print(appliance.heat())

    print("-" * 30)
