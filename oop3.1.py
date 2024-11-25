# 3-нұсқа (Декоратор)
class Component:
    def operation(self):
        return "Негізгі компонент"


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()


class DecoratorA(Decorator):
    def operation(self):
        return f"A({self._component.operation()})"


class DecoratorB(Decorator):
    def operation(self):
        return f"B({self._component.operation()})"

print(DecoratorB(DecoratorA(Component())).operation())  
