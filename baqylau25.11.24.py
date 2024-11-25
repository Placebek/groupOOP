#4 nusqa
# ISP
# Фасад

class Switchable:
    def turn_on(self):
        return "Light is on"

    def turn_off(self):
        return "Light is off"

class DrightnessAdjustable:
    def control_light(self, level):
        return f"Light is {level}"

class TemperatureControllable:
    def control_temperature(self, level):
        return f"Temperature is at home {level}"

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
            self.light.control_light(50), 
            self.temperature.control_temperature(20)
        ]
        return "\n".join(action)
            

control = ControlHome()
print(control.control_home())
