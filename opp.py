# tapsyrma 2
class Message:
    def get_text(self):
    return"Сообщение"

class Decorator(Message):
    def __init__(self,message):
	self.message=message
    def get_text(self):
	return self.message.get_text()

class BoldDecorator(Decorator):
    def get_text(self):
	return f"<b>{self.message.get_text()}</b>"

class ItalicDecorator(Decorator):
    def get_text(self):
	return f"<i>{self.message.get_text()}</i>"

message=Message()
bold_message-BoldDecorator(message)
italic_message = ItalicDecorator(bold_message)
print(italic_message.get_text())

# tapsyrma 1

import math

class Rectangle:
    def __init__(self,width,height):
	self.width=width
	self.height=radius

class Circle:
    def __init__(self,radius):
	self.radius=radius

class AreaCalculator:
    def calculate(self,shape):
	if isinstance(shape,Rectangle):
	    return shape.width*shape.height
	elif isinstance(shape,Circle):
	    return math.pi*shape.radius**2
	else:
	    raise TypeError("Тусиниксиз фигура")
def main():
    rectangle=Rectangle(5,10)
    circle=Circle(7)
    calculator=AreCalculator()

    print(f"Тиктортбурыш ауданы:{calculator.calculate(rectangle)}")
    print(f"Шаршы ауданы:{calculator.calculate(circle)})
if __name__ =="__main__":
    main()