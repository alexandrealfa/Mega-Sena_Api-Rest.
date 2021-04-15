from . import db
from datetime import datetime

class GamesModel(db.Model):
    __tablename__ = "Gamers"
    sort_numbers = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    sorted_numbers = db.Column(db.String, nullable=True)
    create_at = db.Column(db.DateTime, default = datetime.datetime.utcnow())

