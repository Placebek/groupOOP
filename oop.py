
# нұсқа 1

class Vehicle:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, new_speed):
          self.__speed = new_speed

    def set_color(self, new_color):
          self.__color = new_color

    def get_speed(self):
          return self.__speed

     
class Car(Vehicle):
    def drive():
        print("Машина едет")

    def move():
        print("Машина двигается")

class Bike(Vehicle):

    def pedal():
        print("Велосипед крутит педали")
	
    def move():
        print("Машина двигается")


class Boat(Vehicle):
    def sail():
        print("Лодка плывет")

    def move():
        print("Машина двигается")