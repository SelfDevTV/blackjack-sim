

from hand import Hand
from card import Card
import uuid


class Person:

    def __init__(self) -> None:
        self.cardsOnTable: list[Hand] = []
        self.totalValueOnTable = 0
        self.wonCount = 0
        self.tieCount = 0
        self.lostCount = 0
        self.blackjacks = 0
        self.createHand()

    # for all hands
    def getTotalValueOnTable(self):
        value = 0
        for hand in self.cardsOnTable:
            for card in hand.cards:
                value += card.numValue

        return value

    def createHand(self, cards: list[Card] = []):
        newHand = Hand(cards)
        self.cardsOnTable.append(newHand)

    def resetCards(self):
        self.cardsOnTable = []
        self.createHand()
        # for hand in self.cardsOnTable:
        #     hand.resetCardsInHand()

    def printCardsOnTable(self):
        print("All Cards on Table for Person:")
        for hand in self.cardsOnTable:
            for card in hand.cards:
                print(f"{card.value} of {card.suit}")

    def receiveCards(self, cards: list[Card], targetHandId: uuid.UUID | None = None):
        if targetHandId == None:
            self.cardsOnTable[0].receiveCardsInHand(cards)
            return

        for hand in self.cardsOnTable:
            if hand.id == targetHandId:
                hand.receiveCardsInHand(cards)
