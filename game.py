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
        self.dealer.resetCards()
        for player in self.players:
            player.resetCards()
            self.dealer.dealCardsTo(player, 2)
            self.dealer.dealCardsTo(self.dealer)

    def playersTurn(self):
        print("players turn")
        for idx, player in enumerate(self.players):
            print(f"current cards on table for player {idx + 1}")
            player.printCardsOnTable()

            nextMove: utils.Action = utils.calculateNextMove(
                player.cardsOnTable, self.dealer.cardsOnTable[0])

            match nextMove:
                case utils.Action.HIT:
                    player.currentAction = nextMove
                    self.dealer.dealCardsTo(player, 1)
                case utils.Action.STAND:
                    player.currentAction = nextMove
                    self.finishedPlayers.append(
                        self.players.pop(idx))
                case utils.Action.BLACKJACK:
                    player.currentAction = nextMove
                    self.finishedPlayers.append(
                        self.players.pop(idx))
                case utils.Action.SURRENDER:
                    player.currentAction = nextMove
                    self.finishedPlayers.append(
                        self.players.pop(idx))
                case utils.Action.BUSTED:
                    player.currentAction = nextMove
                    self.finishedPlayers.append(
                        self.players.pop(idx))
                case utils.Action.SPLIT:
                    player.currentAction = nextMove
                    player.wonCount += 1
                    # TODO: Split() - instead of a single hand implement multiple hands
                    player.currentAction = utils.Action.SPLIT
                    self.finishedPlayers.append(self.players.pop(idx))
            print(f"Next move is: {nextMove.value}")

    def dealerTurn(self):
        print("dealer turn")

        # should dealer even draw next card
        for idx, player in enumerate(self.finishedPlayers):
            print(player.currentAction)
            if utils.Action.STAND == player.currentAction:
                while self.dealer.totalValueOnTable < 17:
                    self.dealer.dealCardsTo(self.dealer)

                # Check the dealers hand
                if self.dealer.hasBlackJack():
                    player.lostCount += 1
                    self.dealer.wonCount += 1
                    self.dealer.blackjacks += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("Dealer won, dealer has blackjack and player doesn't")
                elif self.dealer.totalValueOnTable > 21:
                    player.wonCount += 1
                    self.dealer.lostCount += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("Player won, dealer busted")
                elif player.totalValueOnTable > self.dealer.totalValueOnTable:
                    player.wonCount += 1
                    self.dealer.lostCount += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("Player won")
                elif player.totalValueOnTable < self.dealer.totalValueOnTable:
                    player.lostCount += 1
                    self.dealer.wonCount += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("Player lost")
                # else its a tie

                else:
                    player.tieCount += 1
                    self.dealer.tieCount += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("It's a tie")
            elif utils.Action.BLACKJACK == player.currentAction:
                # TODO: Figure out actions when player has blackjack
                if self.dealer.hasBlackJack():
                    player.tieCount += 1
                    player.blackjacks += 1
                    self.dealer.tieCount += 1
                    self.dealer.blackjacks += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print("Tied, dealer has blackjack and player has blackjack")
                else:
                    player.wonCount += 1
                    player.blackjacks += 1
                    self.dealer.lostCount += 1
                    print("player cards: ")
                    player.printCardsOnTable()
                    print("dealer cards: ")
                    self.dealer.printCardsOnTable()
                    print(
                        "Player Won, dealer has not a blackjack and player has blackjack")
            else:
                player.lostCount += 1
            self.players.append(self.finishedPlayers.pop(idx))

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
        print(
            f"players count for players {len(self.players)}, count for finish players: {len(self.finishedPlayers)}")
        print(
            f"Game is now over, total player wins: {self.players[0].wonCount}, total player lost {self.players[0].lostCount}, total player tied {self.players[0].tieCount}")

    def start(self):
        self.gameLoop()

    def printHello(self) -> None:
        print("hello from game")
