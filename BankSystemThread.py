import threading
import Database
import socket

class BankSystemThread(threading.Thread):
	def __init__(self, sock, db):
		threading.Thread.__init__(self)
		self.sock = sock
		self.db = db

	def run(self):
		account = None
		while True:
			parts = str(self.sock.recv(40).decode('utf-8')).split()
		
			if (parts[0] == "exit"): 
				break
		
			if account == None:
				if parts[0] == "sign":
					if parts[1] == "in":
						account = self.db.getAccount(parts[2], int(parts[3]), int(parts[4]))
						if account == None: 
							self.sock.send("-1".encode('utf-8'))
						else:
							self.sock.send("0".encode('utf-8'))
					else:
						account = self.db.addAccount(parts[2], int(parts[3]))
						self.sock.send(str(account.card_ID).encode('utf-8'))
			else:	
				if parts[0] == "amount":
					self.sock.send(str(account.getAmount()).encode('utf-8'))
				
				if parts[0] == "get":
					result = account.withdrawMoney(int(parts[1]))
					if result == -1:
						self.sock.send("Error".encode('utf-8'))
					else:
						self.sock.send(str(result).encode('utf-8'))
		
				if parts[0] == "put":
					result = account.addMoney(int(parts[1]))
					self.sock.send(str(result).encode('utf-8'))
			
		self.sock.close()