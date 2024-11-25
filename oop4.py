class DeliverStrategy:
	def deliver_price(self, price):
		return price


class CourierDelivery(DeliverStrategy):
	def deliver_price(self, price):
		return price + 300


class DroneDelivery(DeliverStrategy):
	def deliver_price(self, price):
		return price + 500


def notification(price, deliver_strategy: DeliverStrategy):
	return price


courier_delivery = CourierDelivery()
drone_delivery = DroneDelivery()




#Мост
class Control:
	def __init__(self, device):
		self.device = device

	def turn_on(self):
		return self.device.enable()

	def turn_off(self):
		return self.device.disable()


class TV:
	def enable(self):
		return "Қосылды"
	
	def disable(self):
		return "Өшті"


class Radio:
	def enable(self):
		return "Қосылды"
	
	def disable(self):
		return "Өшті"


tv = TV()
radio = Radio()

control1 = Control(tv)
control2 = Control(radio)

print(control1.turn_on())
print(control2.turn_off())