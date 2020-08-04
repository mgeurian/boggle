from flask import Flask, render_template, request, jsonify, session
from boggle import Boggle


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

boggle_game = Boggle()

@app.route("/")
def home():
    """Show the board"""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    return render_template("index.html", board=board, highscore=highscore, numplays=numplays)

@app.route("/check-word")
def check_word():

    word = request.args['word']
    board = session["board"]
    res = boggle_game.check_valid_word(board, word)

    return jsonify({'result': res})


@app.route("/post-score", methods=["POST"])
def post_score():
    score = request.json["score"]
    print(score)
    highscore = session.get("highscore", 0)
    numplays = session.get("numplays", 0)

    session['numplays'] = numplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(recordBreaker=score > highscore)


