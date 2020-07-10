from random import shuffle
from card import Card

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        amt = min(count, num)
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-amt:]
        self.cards = self.cards[:-amt]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if len(self.cards) == 52:
            shuffle(self.cards)
            return self.cards
        else:
            raise ValueError("Only full decks can be shuffled")

# deck = Deck()
# print(deck.shuffle())
