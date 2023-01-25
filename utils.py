from enum import Enum
from card import Card

class Action(Enum):
    HIT = "HIT"
    STAND = "STAND"
    SURRENDER = "SURRENDER"
    SPLIT = "SPLIT"


# gets passed in cards and then decides what to do next
def calculateNextMove(playerCards: list[Card], dealerUpCard: Card)->Action:

    match dealerUpCard.numValue:


        case _:
            return Action.HIT



