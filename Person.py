#3
class Person:
    def __init__(self, health):
        self.health = health

    def get_health(self):
        return f"{self.health} HP"

class Heart:
    def __init__(self, health):
        self.state = Person(health)

    def get_health_info(self):
        return f"Heart with state {self.state.get_health()}"

class Brain:
    def __init__(self, health):
        self.state = Person(health)

    def get_brain_info(self):
        return f"Brain with state {self.state.get_health()}"

State = Heart("100%")
print(State.get_health_info())
