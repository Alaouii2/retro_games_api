from app import app, db
from app.models import Tag, Game, Platform
from flask import jsonify, redirect, request

games = [
    {'id': 0,
     'name': 'Tetris'},
    {'id': 1,
     'name': 'Space invaders'}
]


@app.route('/', methods=['GET'])
def home():
    return redirect('/game/')

@app.route('/game/', methods=['GET'])
def api():
    return jsonify(games)


@app.route('/game/<id>', methods=['GET'])
def api_id(id):
    return jsonify(games[int(id)])


@app.route('/tags/', methods=['GET', 'POST'])
def tags():
    if request.method == 'POST':
        name = request.args.get('name', '')
        t = Tag(name=name)
        db.session.add(t)
        db.session.commit()
        return jsonify(t.serialize)
    else:
        tags = Tag.query.all()
        return jsonify([t.serialize for t in tags])

