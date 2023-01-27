import deck
import dealer
import player
import utils


class Game:
    def __init__(self, roundsToSimulate=1000, numOfPlayers=1) -> None:
        self.roundsToSimulate = roundsToSimulate
        self.currentRound = 0
        self.players = [player.Player()]
        self.finishedPlayers: list[player.Player] = []
        self.deck = deck.Deck()
        self.dealer = dealer.Dealer(self.deck)
        self.gameStatistics = {
            "players": [{
                "player": None,
                "totalWon": 0,
                "totalLost": 0,
                "totalTied": 0,
                "totalBlackJack": 0
            }],
            "dealerWon": 0,
            "dealerLost": 0,
            "dealerTied": 0,
            "dealerBlackJack": 0
        }

    def newGameInit(self):
        # clear table and init game
        print("clear table and init game")
        self.dealer.resetCards()
        for player in self.players:
            player.resetCards()
            self.dealer.dealCardsTo(player, 2)
            self.dealer.dealCardsTo(self.dealer)

    def playersTurn(self):
        print("players turn")
        print(f"total of players: {len(self.players)}")
        for idx, player in enumerate(self.players):
            print(f"total of hands for player: {len(player.cardsOnTable)}")

            while not len(player.cardsOnTable) == 0:
                for hand in player.cardsOnTable:
                    print(f"current cards on hand for player {idx + 1}")
                    print(f"Loop count: {self.currentRound}")
                    print(hand.printCardsInHand())
                    nextMove: utils.Action = utils.calculateNextMove(
                        hand.get_cardsInHand(), self.dealer.getUpCard())
                    print(f"Next move extracted: {nextMove}")
                    # TODO: don't add player to finished if he still has some hands pending
                    match nextMove:
                        case utils.Action.HIT:
                            hand.currentAction = nextMove
                            self.dealer.dealCardsTo(player, 1, hand.id)
                        case utils.Action.STAND:
                            hand.currentAction = nextMove
                            player.finishHandWithId(hand.id)
                        case utils.Action.BLACKJACK:
                            hand.currentAction = nextMove
                            player.finishHandWithId(hand.id)
                        case utils.Action.SURRENDER:
                            hand.currentAction = nextMove
                            player.finishHandWithId(hand.id)
                        case utils.Action.BUSTED:
                            hand.currentAction = nextMove
                            player.finishHandWithId(hand.id)
                        case utils.Action.SPLIT:
                            if (len(hand.cards) != 2):
                                raise Exception(
                                    "Action is split, but hand card count is not 2")
                            player.splitCount += 1
                            newSplit = [hand.cards.pop()]
                            player.createHand(newSplit)
                            hand.currentAction = utils.Action.HIT

                    print(f"Next move is: {nextMove.value}")
            self.finishedPlayers.append(self.players.pop(idx))
            # self.finishedPlayers.append(self.players.pop(idx))
        # TODO: Figure out bug here - might have something to do with the finished hand array
        print("hello world")

    def dealerTurn(self):
        print("dealer turn")

        if len(self.finishedPlayers) == 0:
            print("no more finished players")

        # should dealer even draw next card
        for idx, player in enumerate(self.finishedPlayers):
            if (len(player.finishedHands) == 0):
                print("no more cards on table")
            for hand in player.finishedHands:
                print(hand.currentAction)

                # TODO: why pop error when action is stand?
                if utils.Action.STAND == hand.currentAction:
                    while self.dealer.getTotalValueOnTable() < 17:
                        self.dealer.dealCardsTo(self.dealer)

                    # Check the dealers hand
                    if self.dealer.hasBlackJack():
                        player.lostCount += 1
                        self.dealer.wonCount += 1
                        self.dealer.blackjacks += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("Dealer won, dealer has blackjack and player doesn't")
                    elif self.dealer.getTotalValueOnTable() > 21:
                        player.wonCount += 1
                        self.dealer.lostCount += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("Player won, dealer busted")
                    elif hand.totalValueInHand > self.dealer.getTotalValueOnTable():
                        player.wonCount += 1
                        self.dealer.lostCount += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("Player won")
                    elif hand.totalValueInHand < self.dealer.getTotalValueOnTable():
                        player.lostCount += 1
                        self.dealer.wonCount += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("Player lost")
                    # else its a tie

                    else:
                        player.tieCount += 1
                        self.dealer.tieCount += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("It's a tie")
                elif utils.Action.BLACKJACK == hand.currentAction:
                    # TODO: Figure out actions when player has blackjack
                    if self.dealer.hasBlackJack():
                        player.tieCount += 1
                        player.blackjacks += 1
                        self.dealer.tieCount += 1
                        self.dealer.blackjacks += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print("Tied, dealer has blackjack and player has blackjack")
                    else:
                        player.wonCount += 1
                        player.blackjacks += 1
                        self.dealer.lostCount += 1
                        print("player cards: ")
                        hand.printCardsInHand()
                        print("dealer cards: ")
                        self.dealer.printCardsOnTable()
                        print(
                            "Player Won, dealer has not a blackjack and player has blackjack")
                else:

                    print(
                        f"player lost we are in else somehow action is: {hand.currentAction}")
                    player.lostCount += 1

        self.players = self.finishedPlayers.copy()
        self.finishedPlayers = []

    # One Game - ends until all players have won / tied or lost

    def newGamePlay(self):
        # while there are players left, keep playing
        while len(self.players) > 0:
            # Check Player Total Val if still in game
            self.playersTurn()
        # Players are gone dealer turn
        self.dealerTurn()

    def gameLoop(self):
        while self.currentRound < self.roundsToSimulate:

            self.newGameInit()
            self.newGamePlay()
            print(f"next round: {self.currentRound}")
            self.currentRound += 1

        self.finishedPlayers = self.players.copy()
        self.players = []
        print(
            f"players count for players {len(self.players)}, count for finish players: {len(self.finishedPlayers)}")
        print(
            f"Game is now over, total player wins: {self.finishedPlayers[0].wonCount}, total player lost {self.finishedPlayers[0].lostCount}, total player tied {self.finishedPlayers[0].tieCount}, total player splitted {self.finishedPlayers[0].splitCount}")

    def start(self):
        self.gameLoop()

    def printHello(self) -> None:
        print("hello from game")
