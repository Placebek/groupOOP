#5
#1-тапсырма
class Computer:
    def _init_(self,status):
        self.status = status

    def get_info(self):
        return f"Computer: {self.status} "
    
class Processor:
    def __init__(self, status):
        self.status = status
        self.processor = Processor("Состояние оптимальное")

    def get_info(self):
        return f'Processor: {self.processor.get_info()}'

class RAM:
    def __init__(self, status):
        self.status = status
        self.ram = RAM("Состояние оптимальное")

    def get_info(self):
        return f"RAM: {self.ram()} "

class HardDrive:
    def __init__(self, status):
        self.status = status
        self.hard_drive = HardDrive("Состояние оптимальное")


    def get_info(self):
        return f"Hard Drive: {self.hard_drive()} "

class GraphicsCard:
    def __init__(self, status):
        self.status = status
        self.graphics_card = GraphicsCard("Состояние оптимальное")

    def get_info(self):
        return f"Graphics Card: {self.graphics_card()}

computer = Computer()
print(get_info())