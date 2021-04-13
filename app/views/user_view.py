from . import user_schema, users_schema, UserModel, db_manager
from flask_restful import Resource, reqparse, current_app
from http import HTTPStatus


class AllUser(Resource):

    def get(self):
        users = UserModel.query.all()
        serializers = users_schema(users)

        return {
            "msg": "success",
            "data": serializers
        }, HTTPStatus.OK


class User(Resource):
    def get(self, user_id):
        current_user = UserModel.query.get_or_404()
        serializer = user_schema(current_user)

        return{
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str, required=True)
        parse.add_argument("phone", type=str, required=True)
        parse.add_argument("email", type=str, required=True)
        parse.add_argument("profile_picture_link", type=str, required=True)
        parse.add_argument("password", type="str", required=True)

        kwargs = parse.parse_args()
        new_user = UserModel(**kwargs)
        db_manager(new_user)
        serializer = user_schema(new_user)

        return {
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    def patch(self, user_id):
        parse = reqparse.RequestParser()
        parse.add_argument("name", type=str)
        parse.add_argument("phone", type=str)
        parse.add_argument("email", type=str)
        parse.add_argument("profile_picture_link", type=str)
        parse.add_argument("password", type=str)

        kwargs = parse.parse_args()
        current_user = UserModel.query.get(user_id)
        if not current_user:
            return {"msg": "user not found!."}, HTTPStatus.NOT_FOUND

        [setattr(current_user, key, value) for key, value in
         kwargs.items() if key is not "password"]
        if kwargs.password:
            current_user.password = kwargs['password']
        db_manager(current_user)
        serializer = user_schema(current_user)

        return{
            "msg": "success",
            "data": serializer
        }, HTTPStatus.OK

    def delete(self, user_id):
        current_user = UserModel.query.get_or_404(user_id)
        db_manager(current_user, True)

        return {
            "msg": f"user {user_id} has been deleted",
        }, HTTPStatus.OK
