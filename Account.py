import Card

class Account:
	def __init__(self, data):
		self.client_ID = int(data[0])
		self.client_name = data[1].get("client_name")
		self.cards = []
		for card_data in data[1].get("cards"):
			self.cards.append(Card.Card(card_data))
	
	def __str__(self):
		result = "_Client:_\n" + self.client_name +  ", id = " + str(self.client_ID) + "\n_Cards:_\n"
		for card in self.cards:
			result += card.__str__() + "\n"
		return result
		
	def getData(self):
		cards_data = []
		for card in self.cards:
			cards_data.append(card.getData())
		return [self.client_ID, {"client_name" : self.client_name, "cards" : cards_data}]
	
	def getCard(self, card_ID, pin_code):
		for card in self.cards:
			if card.card_ID == card_ID:
				if card.pin_code == pin_code:
					return (0, card)
				else:
					return (-1, None)
		return (None, None)
		
	def addCard(self, pin_code):
		newCard = Card.Card({"card_ID" : str(len(self.cards) + 1), "pin_code" : pin_code, "money" : "0"})
		self.cards.append(newCard)
		return newCard