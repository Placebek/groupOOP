# 4-нұсқа (Фасад)
class Light: 
    def on(self): print("Шамды қосу")
    def off(self): print("Шамды өшіру")
    def brightness(self, level): print(f"Brightness: {level}")

class Thermostat: 
    def set_temp(self, temp): print(f"Temperature: {temp}°C")

class Speaker: 
    def play(self, track): print(f"Playing: {track}")
    def stop(self): print("Музыка тоқтады")

class SmartHomeFacade:
    def __init__(self): 
        self.light = Light(); self.thermostat = Thermostat(); self.speaker = Speaker()

    def evening_mode(self): 
        self.light.on(); self.light.brightness(50)
        self.thermostat.set_temp(22)
        self.speaker.play("Кешкі Ойнату Тізімі")

    def stop_mode(self): 
        self.light.off(); self.speaker.stop()

home = SmartHomeFacade()
home.evening_mode()
home.stop_mode()
