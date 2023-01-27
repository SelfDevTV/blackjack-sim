from card import Card
import uuid
import utils


class Hand:
    def __init__(self, cards: list[Card] | None) -> None:
        self.id = uuid.uuid4()
        self.cards: list[Card] = cards or []
        self.totalValueInHand = 0
        self.currentAction: utils.Action = utils.Action.HIT
        # how many different hands the player has if he has splited

    def hasBlackJack(self) -> bool:
        if len(self.cards) == 2 and self.totalValueInHand == 21:
            return True
        else:
            return False

    def get_cardsInHand(self):
        return self.cards

    def receiveCardsInHand(self, cards: list[Card]):
        self.cards.extend(cards)
        for card in cards:
            self.totalValueInHand += card.numValue

    def printCardsInHand(self):
        print(f"Cards in Hand with id {self.id}")
        for card in self.cards:
            print(f"{card.value} of {card.suit}")

    def resetCardsInHand(self):
        self.cards = []
        self.totalValueInHand = 0
