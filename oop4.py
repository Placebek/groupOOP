# 4-нұсқа (ISP)
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class BrightnessAdjustable(ABC):
    @abstractmethod
    def set_brightness(self, level: int):
        pass

class TemperatureControllable(ABC):
    @abstractmethod
    def set_temperature(self, temperature: int):
        pass

class SmartLamp(Switchable, BrightnessAdjustable):
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True
        print("Смарт Шам қазір ҚОСУЛЫ.")

    def turn_off(self):
        self.is_on = False
        print("Ақылды Шам қазір ӨШІРУЛІ.")

    def set_brightness(self, level: int):
        if self.is_on:
            self.brightness = level
            print(f"Смарт Шамның жарықтығы келесіге орнатылады {level}.")
        else:
            print("Ақылды Шам өшірулі. Жарықтықты реттеу мүмкін емес.")

class SmartThermostat(Switchable, TemperatureControllable):
    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def turn_on(self):
        self.is_on = True
        print("Ақылды Термостат ҚАЗІР ҚОСУЛЫ.")

    def turn_off(self):
        self.is_on = False
        print("Ақылды Термостат ҚАЗІР ӨШІРУЛІ.")

    def set_temperature(self, temperature: int):
        if self.is_on:
            self.temperature = temperature
            print(f"Ақылды Термостат температурасы орнатылған {temperature}°C.")
        else:
            print("Ақылды Термостат ӨШІРУЛІ. Температураны реттеу мүмкін емес.")

lamp = SmartLamp()
lamp.turn_on()
lamp.set_brightness(75)
lamp.turn_off()

thermostat = SmartThermostat()
thermostat.turn_on()
thermostat.set_temperature(22)
thermostat.turn_off()
