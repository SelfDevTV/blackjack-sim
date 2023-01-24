from person import Person

class Dealer(Person):
    def __init__(self, deck) -> None:
        Person.__init__(self)
        self.deck = deck
        self.nextCard = None

    def dealCardsTo(self, target: Person, amount=1):
        cards = self.deck.getCards(amount)
        target.receiveCards(cards)

    