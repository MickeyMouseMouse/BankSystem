import os.path
import json
import Account

class Database:
	def __init__(self, databaseFile):
		self.databaseFile = databaseFile
		self.accounts = []
		if not os.path.exists(databaseFile): return
		with open(databaseFile, 'r') as db:
			for client in json.load(db).items():
				self.accounts.append(Account.Account(client))

	def _update_(self):
		data = {}
		for account in self.accounts:
			result = account.getData()
			data[result[0]] = result[1]
		with open(self.databaseFile, 'w') as db:
				json.dump(data, db)

	def getAccount(self, client_ID):
		for account in self.accounts:
			if account.client_ID == client_ID:
				return account
		return None

	def addAccount(self, client_name):
		newAccount = Account.Account((len(self.accounts) + 1, {"client_name" : client_name, "cards" : []}))
		self.accounts.append(newAccount)
		return newAccount