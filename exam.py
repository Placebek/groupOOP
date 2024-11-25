from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def set_width(self, width: int):
        self.width = width
    
    def set_height(self, height: int):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Squar(Shape):
    def __init__(self, side: int):
        self.side = side

    def set_width(self, side: int):
        self.side = side

    def get_area(self):
        return self.side * self.side

def print_area(shape:Shape):
    print("Площадь: ", shape.get_area())

rect = Rectangle(5, 10)
sq = Squar(5)

print_area(rect)
print_area(sq)


#2ex

class Message(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class TextMessage(Message):
    def __init__(self, content: str):
        self.content = content
     
    def render(self) -> str:
        return self.content

class MessageDecorator(Message):
    def __init__(self, wrapped: Message):
        self.wrapped = wrapped
    
    def render(self) -> str:
        return self.wrapped.render()

class EncrytedMessage(MessageDecorator):
    def render(self) -> str:
        original = self.wrapped.render()
        encrypted = original[::-1]
        return f"[Encrypted] {encrypted}"

class CompressedMessage(MessageDecorator):
    def render(self) -> str:
        original = self.wrapped.render()
        compressed = original.replace(" ","")
        return f"[Compressed] {compressed}"

if __name__ == "__main__":
    message = TextMessage("Hello world")
    
    encry = EncrytedMessage(message)
    print(encry.render())
    
    compre = CompressedMessage(message)
    print(compre.render())
    