from deck import CARD_DICT

class Person:
    
    def __init__(self) -> None:
        self._cardsOnTable = []
        self.totalValueOnTable = 0

    def get_cardsOnTable(self):
        return self._cardsOnTable

    def receiveCards(self, cards):
        self._cardsOnTable.append(cards)
        # also change the value
        print("cards: ")
        print(cards)
        for card in cards:
            self.totalValueOnTable += CARD_DICT[str(card["value"])]

    cardsOnTable = property(get_cardsOnTable)

