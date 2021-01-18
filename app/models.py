from app import db


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    games = db.relationship("Game", backref="platform", lazy='dynamic')
    logo_url = db.Column(db.String(200))

    def __repr__(self):
        return f"<Platfrom {self.name}"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    platform_id = db.Column(db.Integer, db.ForeignKey("platform.id"))
    poster_url = db.Column(db.String(200))

    def __repr__(self):
        return f"<Game {self.name}>"


class Tag(db.Models):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True) 
