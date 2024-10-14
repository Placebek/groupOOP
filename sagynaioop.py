class Appliance:
    def__init__(self, brand, power)
    self.__brand = brand
    self.__power = power
    
    def get_brand(self):
        return self.__brand

    def set_brand(self):
        self.__brand = brand

    def get_power(self):
        return self.__power

    def set_power(self):
        self.__power = power

class WashingMachine(Appliance):
    def wash(self):
	return "Стиральная машина стирает"

class Refrigerator(Appliance):
    def cool(self):
	return "Холодильник охлаждает"

class Microwave(Appliance):
    def heat(self)
	return "Микроволновка разогревает еду"

def operate():
    washingmachine = WashingMachine("LG washing machine", "on")
    refrigerator = Refrigerator("SAMSUNG refrigerator", "on")
    microwave = Microwave("LG microwave", "on")

print(operate.washingmachine)
print(operate.refrigerator)
print(operate.microwave)