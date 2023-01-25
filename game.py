from deck import Deck
from dealer import Dealer
from player import Player

class Game:
    def __init__(self, roundsToSimulate = 1, numOfPlayers=1) -> None:
        self.roundsToSimulate = roundsToSimulate
        self.currentRound = 0
        self.players = [Player()]
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.gameStatistics = {
            "players": [{
                "player": None, 
                "totalWon": 0,
                "totalLost": 0,
                "totalTied": 0
            }],
            "dealerWon": 0,
            "dealerLost": 0,
            "dealerTied": 0,
        }

    def newGameInit(self):
        for player in self.players:
            self.dealer.dealCardsTo(player, 2)
            self.dealer.dealCardsTo(self.dealer)

    # One Game - ends until all players have won / tied or lost
    def newGamePlay(self):
        # while there are players left, keep playing
        while len(self.players) > 0:
            # TODO: Create main game logic
            self.players.pop()
            print("play game")

    def gameLoop(self):
        while self.currentRound < self.roundsToSimulate:
            self.newGameInit()
            self.newGamePlay()
            self.currentRound += 1

    def start(self):
        self.gameLoop()

    def printHello(self) -> None:
        print("hello from game")