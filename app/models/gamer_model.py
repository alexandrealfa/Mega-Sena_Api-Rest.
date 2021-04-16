from datetime import datetime

from . import db


class GameModel(db.Model):
    __tablename__ = "games"
    id = db.Column(db.Integer, primary_key=True)
    sort_numbers = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    sorted_numbers = db.Column(db.String, nullable=True)
    mega_result = db.Column(db.String, nullable = True)
    correct_numbers = db.Column(db.String, nullable = True)
    result_sort = db.Column(db.String, nullable=True)
    create_at = db.Column(db.DateTime, default = datetime.utcnow())

