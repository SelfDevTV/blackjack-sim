import json
import random 


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

class Deck:
    def __init__(self) -> None:
        self.cards = []
        self._cardsLeft = len(self.cards)
        self.generateCards()
        self.shuffleCards()

    def get_cardsLeft(self):
        return len(self.cards)


    def generateCards(self):
        with open('deck.json') as d:
            cardsJson = json.load(d)
            for card in cardsJson:
                self.cards.append(card)
            

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