from random import shuffle

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		
	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"] 
		values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		self.cards = [Card(suit, value) for suit in suits for value in values]
		#print(self.cards)

	def __repr__(self):
		return "Deck of {} cards".format(self.count())

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count, num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

		print("Removing {} cards from the deck".format(actual))
	
	def shuffle(self):
		if self.count() < 52:
			raise  ValueError("Only a full deck of cards can be shuffled")
		shuffle(self.cards)
		return self 

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, num_cards):
		return self._deal(num_cards)

#instanciating new deck of cards and shuffling
d = Deck()
d.shuffle()

#dealing player's cards
hole_cards = d.deal_hand(2)
print(hole_cards)

#proving deck is correct 
print(d.count())















