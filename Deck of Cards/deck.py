class Deck:
    number_of_cards_in_new_deck = 52
    current_deck = []

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"Deck of {len(Deck.current_deck)} cards."
    
    def _deal(self, number_to_deal):
        try:
            return [c for c in range(self.number_to_deal, self.current_deck)]
        except ValueError:
            return "All cards have been dealt"

    def count(self):
        return len(Deck.current_deck)
    
