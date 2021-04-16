from datetime import timedelta
from http import HTTPStatus

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from . import UserModel, user_schema


class SignIn(Resource):
    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("password", type=str, required=True)
        kwargs = parse.parse_args()
        email = [value for key, value in kwargs.items() if key == "email"][0]
        found_user = UserModel.query.filter_by(email=email).first()
        if not found_user:
            return {"msg": "User Not Found!."}, HTTPStatus.NOT_FOUND
        access_token = create_access_token(identity=found_user.id, expires_delta=timedelta(days=7))
        if not found_user.check_password(kwargs.password):
            return {"msg": "invalid Password"}, HTTPStatus.UNAUTHORIZED
        serializer = user_schema.dump(found_user)
        return {"msg": "created", "data": serializer, "access_token": access_token}, HTTPStatus.OK
