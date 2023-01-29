from flask import Flask, request
from flask_cors import CORS, cross_origin
import game


app = Flask(__name__)
CORS(app, support_credentials=True)



@app.route("/")
@cross_origin(origin="*")
def get_dealer_wins():
    roundsToSimulate = int(request.args.get('roundsToSimulate'))
    numOfPlayers = int(request.args.get('numOfPlayers'))
    # TODO: Check args
    newGame = game.Game(roundsToSimulate=roundsToSimulate,
                        numOfPlayers=numOfPlayers)
    newGame.start()
    stats = newGame.getStatistics()
    return stats
