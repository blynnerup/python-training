import random
from card import Card

class Deck:
    number_of_cards_in_new_deck = 52
    current_deck = []

    def __init__(self):
        suits = ['♠', '♦', '♥', '♣']
        values =[num for num in range(2,11)]
        face_value = ['J',"K","Q","A"]
        values.extend(face_value)
        self.cards = [Card(value, suit) for value in values for suit in suits]
        
    def __repr__(self) -> str:
        return f"Deck of {len(self.cards)} cards"   

    def count(self):
        return len(self.cards)
    
    def _deal(self, deal_cards):
        try:
            hand = self.cards[-deal_cards:]
            self.cards = self.cards[:-deal_cards]
        except ValueError:
            return "All cards have been dealt"
        return hand
    
    def deal_card(self):
        return self._deal(1)
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
                           
    
d = Deck()
d.shuffle()
print(d.count())
print(d)
print(d.deal_card())
print(d)
print(d.deal_hand(5))
print(d)
# d.shuffle()
