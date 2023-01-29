import json
import random
from card import Card
from pathlib import Path

THIS_FOLDER = Path(__file__).parent.resolve()
deckCsvPath = THIS_FOLDER/"static/deck.json"


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self._cardsLeft = len(self.cards)
        self.shuffleCount = 0
        self.generateCards()
        self.shuffleCards()

    def get_cardsLeft(self):
        return len(self.cards)

    def generateCards(self):
        self.shuffleCount += 1
        self.cards = []
        with open(deckCsvPath) as d:
            cardsJson = json.load(d)
            for card in cardsJson:
                newCard = Card(card["value"], card["suit"])
                self.cards.append(newCard)

    def resetDeck(self):
        self.generateCards()
        self.shuffleCards()

    def shuffleCards(self):

        random.shuffle(self.cards)

    # Returns array of card(s) or empty array if deck would be empty

    def getCards(self, amount=1):
        cardsToReturn = []
        if len(self.cards) >= amount:
            for i in range(amount):
                cardsToReturn.append(self.cards.pop())
        return cardsToReturn

    cardsLeft = property(get_cardsLeft)
