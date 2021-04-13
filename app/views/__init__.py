from app.models.user_model import UserModel
from app.schema.user_schema import user_schema, users_schema
from flask import current_app


def db_manager(current_model: object, delete: bool = False):
    session = current_app.db.session

    if delete:
        session.delete(current_model)
        session.commit()

    if not delete:
        session.add(current_model)
        session.commit()