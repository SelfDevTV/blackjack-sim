CARD_DICT = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10,
    "A": 11
}

class Card:
    def __init__(self, value, suit) -> None:
        self.value: str = value
        self.suit: str = suit
        self.numValue: int = CARD_DICT[str(value)]