from shortner import db


class Shortner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False, unique=True)
    short = db.Column(db.String(100), unique=True)