from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    profile_picture = db.Column(db.String, nullable=True)
    password_hash = db.Column(db.String, nullable=False)
    game_list = db.relationship("GameModel", backref=db.backref("user_play", lazy="joined"), lazy ="joined")


    
    @property
    def password(self):
        raise TypeError("Password cannot be accessed")

    @password.setter
    def password(self, new_user_password):
        new_password_hash = generate_password_hash(new_user_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)