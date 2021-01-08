import os.path
import Account

class Database:
	def __init__(self, databaseFile):
		self.databaseFile = databaseFile
		self.data = []
		if not os.path.exists(databaseFile): return
		with open(databaseFile, 'r') as db:
			for line in db:
				parts = line.split()
				self.data.append(Account.Account(parts[0], parts[1], parts[2], parts[3]))

	def save(self):
		with open(self.databaseFile, 'w') as db:
			for account in self.data:
				db.write(account.__str__() + "\n")

	def getAccount(self, client_ID, card_ID, pin_code):
		for account in self.data:
			if account.equals(client_ID, card_ID, pin_code):
				return account
		return None

	def addAccount(self, client_ID, pin_code):
		newAccount = Account.Account(client_ID, len(self.data) + 1, pin_code, 0)
		self.data.append(newAccount)
		return newAccount