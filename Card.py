import threading

class Card:
	def __init__(self, data):
		self.card_ID = int(data.get("card_ID"))
		self.pin_code = int(data.get("pin_code"))
		self.money = int(data.get("money"))
		
		self.lock = threading.Lock() # to synchronize threads
	
	def __str__(self):
		return  str(self.card_ID) + " " + str(self.pin_code) + " " + str(self.money)

	def getData(self):
		return {"card_ID" : str(self.card_ID), "pin_code" : str(self.pin_code), "money" : str(self.money)}
	
	def getAmount(self):
		self.lock.acquire(1)
		
		result = self.money
		
		self.lock.release()
		return result
	
	def withdrawMoney(self, amount):
		self.lock.acquire(1)
		
		result = -1
		if self.money >= amount:
			self.money -= amount
			result = self.money
		
		self.lock.release()
		return result
			
	def addMoney(self, amount):
		self.lock.acquire(1)
		
		self.money += amount
		result = self.money
		
		self.lock.release()
		return result