import deck
import dealer
import player
import utils
import uuid


class Game:
    def __init__(self, roundsToSimulate=10000, numOfPlayers=1) -> None:
        self.roundsToSimulate = roundsToSimulate
        self.currentRound = 0
        self.players = self.initPlayers(numOfPlayers)
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

    def initPlayers(self, numOfPlayers: int):
        players = []
        for i in range(numOfPlayers):
            newPlayer = player.Player()
            players.append(newPlayer)
        return players

    def newGameInit(self):
        # clear table and init game
        print("clear table and init game")
        self.dealer.resetCards()
        self.dealer.dealCardsTo(self.dealer)
        for player in self.players:
            player.resetCards()
            self.dealer.dealCardsTo(player, 2)

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
            self.finishedPlayers.append(self.players.pop(idx))
            # self.finishedPlayers.append(self.players.pop(idx))

    def dealerTurn(self):
        print("dealer turn")
        print("dealer cards: ")
        self.dealer.printCardsOnTable()

        if len(self.finishedPlayers) == 0:
            print("no more finished players")

        # should dealer even draw next card
        for idx, player in enumerate(self.finishedPlayers):
            if (len(player.finishedHands) == 0):
                print("no more cards on table")
            for hand in player.finishedHands:
                print(hand.currentAction)

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

    def printStatistics(self):
        pass
        # TODO: Statistic for dealer

        # TODO: General game statistic

        for player in self.finishedPlayers:
            pass
            # TODO: print Statistic for every player

    def getStatistics(self):
        # make list for serialization
        # TODO: get percent rate of all players combined
        players = []
        for player in self.finishedPlayers:
            playerDict = {
                "id": uuid.uuid4(),
                "wins": player.wonCount,
                "looses": player.lostCount,
                "ties": player.tieCount,
                "blackjack": player.blackjacks,
                "splits": player.splitCount,
                "winRateInPct": (player.wonCount / (self.currentRound + player.splitCount)) * 100,
                "tieRateInPct": (player.tieCount / (self.currentRound + player.splitCount)) * 100,
                "looseRateInPct": (player.lostCount / (self.currentRound + player.splitCount)) * 100
            }
            players.append(playerDict)

        stats = {}
        stats["roundsSimulatedPerPlayer"] = self.roundsToSimulate
        stats["roundsSimulatedTotal"] = self.roundsToSimulate * \
            len(self.finishedPlayers)
        stats["playerCount"] = len(self.finishedPlayers)
        stats["dealerStats"] = {
            "wins": self.dealer.wonCount,
            "looses": self.dealer.lostCount,
            "ties": self.dealer.tieCount,
            "blackjack": self.dealer.blackjacks
        },
        stats["players"] = players

        return stats

        # TODO: Return a dict / object with all statistics

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
        self.printStatistics()
        print(
            f"players count for players {len(self.players)}, count for finish players: {len(self.finishedPlayers)}")

        for player in self.finishedPlayers:
            print(
                f"Game is now over, total player wins: {player.wonCount}, total player lost {player.lostCount}, total player tied {player.tieCount}, total player splitted {player.splitCount}")
            print(
                f"% win rate: {(player.wonCount / (self.currentRound + player.splitCount)) * 100}")

    def start(self) -> int:
        self.gameLoop()
        return self.dealer.wonCount
