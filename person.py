

import card


class Person:

    def __init__(self) -> None:
        self._cardsOnTable: list[card.Card] = []
        self.totalValueOnTable = 0
        self.wonCount = 0
        self.tieCount = 0
        self.lostCount = 0
        self.blackjacks = 0

    def hasBlackJack(self) -> bool:
        if len(self._cardsOnTable) == 2 and self.totalValueOnTable == 21:
            return True
        else:
            return False

    def get_cardsOnTable(self):
        return self._cardsOnTable

    def printCardsOnTable(self):
        print("Cards on Table:")
        for card in self._cardsOnTable:
            print(f"{card.value} of {card.suit}")

    def receiveCards(self, cards: list[card.Card]):
        self._cardsOnTable.extend(cards)
        for card in cards:
            self.totalValueOnTable += card.numValue

    def resetCards(self):
        self._cardsOnTable = []
        self.totalValueOnTable = 0

    cardsOnTable = property(get_cardsOnTable)
