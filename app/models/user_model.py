from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    profile_picture = db.Column(db.String, nullable=True)
    password_hash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise TypeError("Password cannot be accessed")

    @password.setter
    def password(self, new_user_password):
        new_password_hash = generate_password_hash(new_user_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)