from flask import current_app

from app.models.gamer_model import GameModel
from app.models.user_model import UserModel
from app.schema.gamer_schema import game_schema, games_schema
from app.schema.user_schema import user_schema, users_schema
from flask import Flask


def init_app(app:Flask):
    pass

def db_manager(current_model: object, delete: bool = False):
    session = current_app.db.session

    if delete:
        session.delete(current_model)
        session.commit()

    if not delete:
        session.add(current_model)
        session.commit()