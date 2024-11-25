# 3-нұсқа (LPS)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


rect = Rectangle(4, 5)
print(f"Тік төртбұрыш ауданы: {rect.area()}")

square = Square(4)
print(f"Шаршы ауданы: {square.area()}")
