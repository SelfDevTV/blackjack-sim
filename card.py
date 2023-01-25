from deck import CARD_DICT

class Card:
    def __init__(self, value, suit) -> None:
        self.value: str = value
        self.suit: str = suit
        self.numValue: int = CARD_DICT[value]