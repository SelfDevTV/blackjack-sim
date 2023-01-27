import person
from deck import Deck
import uuid


class Dealer(person.Person):
    def __init__(self, deck) -> None:
        person.Person.__init__(self)
        self.deck: Deck = deck
        self.nextCard = None

    def getUpCard(self):
        if len(self.cardsOnTable) == 0:
            raise Exception("Dealer has no hands - no cards at all")
        if len(self.cardsOnTable) > 1:
            raise Exception("Dealer has more then one hand which can't be")
        if len(self.cardsOnTable[0].cards) == 0:
            raise Exception(
                "Dealer has exactly one hand but no cards on this hand which can't be")

        return self.cardsOnTable[0].cards[0]

    def hasBlackJack(self):
        return self.cardsOnTable[0].hasBlackJack()

    def dealCardsTo(self, targetPerson: person.Person, amount: int = 1, targetHandId:  uuid.UUID | None = None):
        if self.deck.get_cardsLeft() < amount:
            self.deck.resetDeck()

        cards = self.deck.getCards(amount)
        if targetHandId == None:
            targetPerson.receiveCards(cards)
        else:
            targetPerson.receiveCards(cards, targetHandId)
