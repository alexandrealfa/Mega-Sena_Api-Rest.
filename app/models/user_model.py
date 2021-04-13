from . import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    password_hash = db.Column(db.String, nullable=False)