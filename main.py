from flask import Flask, request
import game


app = Flask(__name__)


@app.route("/")
def get_dealer_wins():
    roundsToSimulate = int(request.args.get('roundsToSimulate'))
    numOfPlayers = int(request.args.get('numOfPlayers'))
    # TODO: Check args
    newGame = game.Game(roundsToSimulate=roundsToSimulate,
                        numOfPlayers=numOfPlayers)
    newGame.start()
    stats = newGame.getStatistics()
    return stats
