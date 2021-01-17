from app import app
from flask import jsonify, redirect

games = [
    {'id': 0,
     'name': 'Tetris'},
    {'id': 1,
     'name': 'Space invaders'}
]


@app.route('/', methods=['GET'])
def home():
    return redirect("/game/")

@app.route('/game/', methods=['GET'])
def api():
    return jsonify(games)


@app.route('/game/<id>', methods=['GET'])
def api_id(id):
    return jsonify(games[int(id)])
