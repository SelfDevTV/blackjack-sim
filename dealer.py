import person
from deck import Deck


class Dealer(person.Person):
    def __init__(self, deck) -> None:
        person.Person.__init__(self)
        self.deck: Deck = deck
        self.nextCard = None

    def dealCardsTo(self, target: person.Person, amount: int = 1):
        if self.deck.get_cardsLeft() < amount:
            self.deck.resetDeck()

        cards = self.deck.getCards(amount)
        target.receiveCards(cards)
