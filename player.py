import person
import uuid
from utils import Action


class Player(person.Person):
    def __init__(self) -> None:
        person.Person.__init__(self)
        self.id = 1

        self.splitCount = 0
        self.finishedHands = []

    def finishHandWithId(self, handId: uuid.UUID):
        print(f"finish hand with id: {handId}")
        for idx, hand in enumerate(self.cardsOnTable):
            if hand.id == handId:
                print(f"id found, hand count before: {len(self.cardsOnTable)}")
                self.finishedHands.append(self.cardsOnTable.pop(idx))
                print(f"id found, hand count after: {len(self.cardsOnTable)}")
            else:
                print(
                    f"id not found, hand count: {len(self.cardsOnTable)}, hand id: {hand.id}")

    def resetCards(self):
        for hand in self.cardsOnTable:
            hand.resetCardsInHand()
        self.cardsOnTable = []
        self.finishedHands = []
        self.createHand()

    def isPlayerFinished(self) -> bool:
        for hand in self.cardsOnTable:
            if hand.currentAction.HIT:
                return False
            print("player finished with all hands")
        return True
