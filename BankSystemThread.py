import threading
import socket

class BankSystemThread(threading.Thread):
	def __init__(self, sock, db):
		threading.Thread.__init__(self)
		self.sock = sock
		self.sock.settimeout(1.5)  
		self.db = db
		self.stop_event = threading.Event()

	def sendMessage(self, msg):
		try:
			self.sock.send(msg.encode('utf-8'))
		except socket.error:
			self.stop_event.set()

	def run(self):
		account = None
		card = None
		while True:
			if self.stop_event.is_set(): break
			
			try:
				parts = str(self.sock.recv(40).decode('utf-8')).split()
				if len(parts) == 0: # client is dead
					self.stop_event.set()
					continue
			except socket.timeout:
				continue
				
			if (parts[0] == "exit"): 
				break
		
			if account == None:
				if parts[0] == "sign":
					if parts[1] == "in":
						account = self.db.getAccount(int(parts[2]))
						if account == None: 
							self.sendMessage("-1")
						else:
							self.sendMessage(account.client_name)
					else:
						account = self.db.addAccount(parts[2])
						self.sendMessage(str(account.client_ID))
			else:	
				if parts[0] == "select":
					status, card = account.getCard(int(parts[1]), int(parts[2]))
					if status == None: self.sendMessage("No card with this id")
					if status == -1: self.sendMessage("Wrong password")
					if status == 0: self.sendMessage("Done")
				
				if parts[0] == "new":
					card = account.addCard(parts[1])
					self.sendMessage("Card id is " + str(card.card_ID))
				
				if parts[0] == "amount":
					if card != None:
						self.sendMessage(str(card.getAmount()))
					else:
						self.sendMessage("First select your card")
				
				if parts[0] == "get":
					if card != None:
						result = card.withdrawMoney(int(parts[1]))
						if result == -1:
							self.sendMessage("There is no such money")
						else:
							self.sendMessage(str(result))
					else:
						self.sendMessage("First select your card")					
					
				if parts[0] == "put":
					if card != None:
						result = card.addMoney(int(parts[1]))
						self.sendMessage(str(result))
					else:
						self.sendMessage("First select your card")					
			
		self.sock.close()