from app import db

class Player(db.Model):
    __tablename__ = 'players'

    id   = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    avg  = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Player {self.name!r}>'
