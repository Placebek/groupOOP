#1 нұсқа 2-тапсырма
class CPU:
    def start(self):
        print("Start")

    def execute(self):
        print("Пcompleting tasks")

class Memory:
    def load(self):
        print("loading")

class HardDrive:
    def read(self):
        print("считываються")

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        print("start")
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()
        self.cpu.execute()
        print("ready")

if __name__ == "__main__":
    computer = ComputerFacade()
    computer.start_computer()
