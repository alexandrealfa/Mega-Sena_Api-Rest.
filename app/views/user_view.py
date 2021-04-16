from http import HTTPStatus

from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from . import UserModel, db_manager, user_schema, users_schema


class AllUser(Resource):
    @jwt_required()
    def get(self):
        users = UserModel.query.all()
        serializers = users_schema.dump(users)

        return {
            "msg": "success",
            "data": serializers
        }, HTTPStatus.OK


class User(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        current_user = UserModel.query.get_or_404(user_id)
        serializer = user_schema.dump(current_user)

        return{
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK


    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("profile_picture", type=str, required=True)
        parse.add_argument("password", type=str, required=True)

        kwargs = parse.parse_args()
        
        new_user = UserModel(**kwargs)
        db_manager(new_user)
        serializer = user_schema.dump(new_user)

        return {
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    @jwt_required()
    def patch(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("profile_picture", type=str)
        parse.add_argument("password", type=str)

        kwargs = parse.parse_args()
        current_user = UserModel.query.get(get_jwt_identity())
        if not current_user:
            return {"msg": "user not found!."}, HTTPStatus.NOT_FOUND

        [setattr(current_user, key, value) for key, value in
         kwargs.items() if key != "password" and value is not None]
        if kwargs.password:
            current_user.password = kwargs['password']
        db_manager(current_user)
        serializer = user_schema.dump(current_user)

        return{
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()
        current_user = UserModel.query.get_or_404(user_id)
        db_manager(current_user, True)

        return set(), HTTPStatus.NO_CONTENT
