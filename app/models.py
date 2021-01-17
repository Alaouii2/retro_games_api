from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    poster_url = db.Column(db.String(200))

    def __repr__(self):
        return f"<User {self.name}>"
