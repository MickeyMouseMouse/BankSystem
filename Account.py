import threading

class Account:
	def __init__(self, client_ID, card_ID, pin_code, money):
		self.client_ID = str(client_ID)
		self.card_ID = int(card_ID)
		self.pin_code = int(pin_code)
		self.money = int(money)
		
		self.event = threading.Event() # to synchronize threads
		self.event.set()
	
	def __str__(self):
		return self.client_ID + " " + str(self.card_ID) + " " + str(self.pin_code) + " " + str(self.money)

	def equals(self, client_ID, card_ID, pin_code):
		if (self.client_ID == client_ID and 
			self.card_ID == card_ID and 
			self.pin_code == pin_code): 
			return True
		else:
			return False
	
	def getAmount(self):
		self.event.wait()
		self.event.clear()
		
		result = self.money
		
		self.event.set()
		return result
	
	def withdrawMoney(self, amount):
		self.event.wait()
		self.event.clear()
		
		result = -1
		if self.money >= amount:
			self.money -= amount
			result = self.money
		
		self.event.set()
		return result
			
	def addMoney(self, amount):
		self.event.wait()
		self.event.clear()
		
		self.money += amount
		result = self.money
		
		self.event.set()
		return result