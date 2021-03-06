from app import db

tags = db.Table('tags',
                db.Column('game_id', db.Integer, db.ForeignKey(
                    'game.id'), primary_key=True),
                db.Column('tag_id', db.Integer, db.ForeignKey(
                    'tag.id'), primary_key=True)
                )


class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    games = db.relationship("Game", lazy="dynamic")
    logo_url = db.Column(db.String(200))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'logo_url': self.logo_url,
        }
    
    def __repr__(self):
        return f"<Platform: {self.name}"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True)
    poster_url = db.Column(db.String(200))
    platform_id = db.Column(db.Integer, db.ForeignKey("platform.id"))
    tags = db.relationship(
        'Tag', secondary=tags, lazy='subquery', backref=db.backref('games', lazy=True))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'poster_url': self.poster_url
        }
    
    def __repr__(self):
        return f"<Game: {self.name}>"


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=True)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    
    def __repr__(self):
        return f"Tag: {self.name}"
