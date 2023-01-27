

import enum
import card
# import player


class Action(enum.Enum):
    HIT = "Hit"
    STAND = "Stand"
    SURRENDER = "Surrender"
    SPLIT = "Split"
    BLACKJACK = "Blackjack"
    BUSTED = "Busted"


def cardsHaveAce(cards: list["card.Card"]) -> bool:
    for card in cards:
        if card.value == "A":
            return True

    return False


def cardsShouldBeSplit(cards: list["card.Card"], dealerUpCard: "card.Card") -> bool:
    if len(cards) != 2:
        return False

    firstCard = cards[0]
    secondCard = cards[0]
    if firstCard.value == secondCard.value:
        # Dealer Cards
        match dealerUpCard.numValue:
            case 2:
                # Player Cards
                match firstCard.numValue:
                    case 2, 3, 4, 5, 6:
                        return False
                    case 7, 8, 9:
                        return True
                    case 10:
                        return False
                    case 11:
                        return True
            case 3:
                match firstCard.numValue:
                    case 2, 3, 4, 5:
                        return False
                    case 6, 7, 8, 9:
                        return True
                    case 10:
                        return False
                    case 11:
                        return True
            case 4, 5, 6:
                match firstCard.numValue:
                    case 2, 3:
                        return True
                    case 4, 5:
                        return False
                    case 6, 7, 8, 9:
                        return True
                    case 10:
                        return False
                    case 11:
                        return True
            case 7:
                match firstCard.numValue:
                    case 2, 3:
                        return True
                    case 4, 5, 6:
                        return False
                    case 7, 8:
                        return True
                    case 9, 10:
                        return False
                    case 11:
                        return True
            case 8, 9:
                match firstCard.numValue:
                    case 2, 3, 4, 5, 6, 7:
                        return False
                    case 8, 9:
                        return True
                    case 10:
                        return False
                    case 11:
                        return True
            case 10, 11:
                match firstCard.numValue:
                    case 2, 3, 4, 5, 6, 7:
                        return False
                    case 8:
                        return True
                    case 9, 10:
                        return False
                    case 11:
                        return True

    return False


def dealerShouldRevealCards(players) -> bool:
    for player in players:
        for hand in player.cardsOnTable:
            if hand.currentAction != Action.STAND or hand.currentAction != Action.SURRENDER or hand.currentAction != Action.BLACKJACK:
                return False
    return True


def getTotalValueOfCards(cards: list["card.Card"]) -> int:
    totalValOfCards = 0
    for card in cards:
        totalValOfCards += card.numValue
    return totalValOfCards


def getTotalValueOfCardsAceAsOne(cards: list["card.Card"]) -> int:
    totalValOfcards = 0
    for card in cards:
        if card.value == "A":
            totalValOfcards += 1
        else:
            totalValOfcards += card.numValue
    return totalValOfcards


def calculateHardTotal(numValOfPlayerCards: int, standAt: int = 0) -> Action:
    # stand above
    if numValOfPlayerCards >= standAt:
        return Action.STAND
    # stand below
    else:
        return Action.HIT


def calculateSoftTotal(numValOfPlayerCards: int, standAt: int = 0) -> Action:
    # stand above
    if numValOfPlayerCards >= standAt:
        return Action.STAND
    # stand below
    else:
        return Action.HIT


# gets passed in cards and then decides what to do next
def calculateNextMove(playerCards: list[card.Card], dealerUpCard: card.Card) -> Action:

    numValOfCards = getTotalValueOfCards(playerCards)
    # val of cards when all aces are count as 1 instead of 11
    numValOfCardsAceAsOne = getTotalValueOfCardsAceAsOne(playerCards)
    playerHasAce = cardsHaveAce(playerCards)
    playerHasPair = cardsShouldBeSplit(playerCards, dealerUpCard)

    # Busted
    if numValOfCardsAceAsOne > 21:
        return Action.BUSTED

    # Blackjack
    if len(playerCards) == 2 and numValOfCards == 21:
        return Action.BLACKJACK

    match dealerUpCard.numValue:
        case 2:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=13)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT

        case 3:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=13)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 4:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=12)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 5:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=12)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 6:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=12)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 7:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=17)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 8:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=17)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=18)
            else:
                return Action.SPLIT
        case 9:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=17)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=19)
            else:
                return Action.SPLIT
        case 10:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=17)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=19)
            else:
                return Action.SPLIT
        case 11:
            if not playerHasAce and not playerHasPair:
                # TODO: Always return a action and also make it so it takes one name argument instead
                return calculateHardTotal(numValOfCards, standAt=17)
            elif playerHasAce and not playerHasPair:
                return calculateSoftTotal(numValOfCards, standAt=19)
            else:
                return Action.SPLIT

        case _:
            raise Exception("Cards doesn't match any of the rulesets")

    raise Exception("Cards doesn't match any of the rulesets")
