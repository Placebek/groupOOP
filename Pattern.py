# 5 - нұсқа
from abc import ABC, abstractmethod


class CarComponent(ABC):
    @abstractmethod
    def check_status(self):
        pass


class Engine(CarComponent):
    def check_status(self): return "Engine is working."

class Wheel(CarComponent):
    def check_status(self): return "Wheel is in good condition."

class Seat(CarComponent):
    def check_status(self): return "Seat is clean."


class Car:
    def _init_(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def check_all_components(self):
        for component in self.components:
            print(component.check_status())


def create_component(component_type):
    components = {"engine": Engine, "wheel": Wheel, "seat": Seat}
    return components.get(component_type)()


car = Car()
for comp_type in ["engine", "wheel", "seat"]:
    car.add_component(create_component(comp_type))

car.check_all_components()