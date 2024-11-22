# 1

class Order:
    def __init__(self):
        self.__order_number = 12345
        self.__status = "active"

    def update_status(self, new_status):
        self.__status = new_status

    def get_status(self):
        return self.__status

order = Order()

order.update_status("Not active")
print(order.get_status())




# 2

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_info(self):
        return f"Пользователь: {self.username}, Email: {self.email}."

class Admin(User):
    def __init__(self, username, email, privilegies):
        super().__init(username, email)
        self.privilegies = privilegies

class Customer(User):
    def __init__(self, username, email, purchase_history):
        super().__init(username, email)
        self.purhase_history = purchase_history        

user = User("Darkhan", "darkhan@mail.ru")
print(user.get_info())


# # 3
class Transport:
    def __init__(self, name):
        self.name = name 

    def move(self):
        return f"{self.name}"

class Bicycle(Transport):
    def __init__(self, name):
        super().__init__(name)
        
    def move(self):
        return f"{self.name} is pedaling"

class Car(Transport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        return f"{self.name} is driving"

class Boat(Transport):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        return f"{self.name} is sailing"

b = Bicycle("Bicycle")
print(b.move())

c = Car("Car")
print(c.move())

d = Boat("Boat")
print(d.move()) 