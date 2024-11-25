#4 nusqa
# ISP
# Фасад

class Switchable:
    def turn_on(self):
        print("Light is on")

    def turn_of(self):
        print("Light is off")

class DrightnessAdjustable:
    def control_light(self, level):
        print(f"Light is {level}")

class TemperatureControllable:
    def control_temperature(self, level):
        print(f"Temperature is at home {level}")

# Фасад

class ControlHome:
    def __init__(self):
        self.switch = Switchable()
        self.light = DrightnessAdjustable()
        self.temperature = TemperatureControllable()

    def control_home(self):
        action = [
            self.switch.turn_on(), 
            self.switch.turn_off(), 
            self.light.control_light(), 
            self.temperature.control_temperature()
        ]
        return "\n".join(action)
            

control = ControlHome()
print(control.control_home())
