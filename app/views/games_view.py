from http import HTTPStatus

from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, reqparse

from app.services.compare_string_services import compare_string
from app.services.game_services import game_maker
from app.services.message_services import message_result
from app.services.webscrapping_bot_services import get_ms_result

from . import GameModel, db_manager, game_schema, games_schema, UserModel


class AllGamers(Resource):
    @jwt_required()
    def get(self):
        page =  1 if not request.args.get('page') else int(request.args.get('page'))
        per_page = 15 if not request.args.get('per_page') else int(request.args.get('per_page'))
        all_games = GameModel.query.order_by(GameModel.id).paginate(page=page, per_page=per_page, error_out=False).items
        serializer = games_schema.dump(all_games)

        return {"data": serializer}, HTTPStatus.OK


class Games(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()

        all_games = GameModel.query.filter(GameModel.user_id == user_id).all()

        serializer = games_schema.dump(all_games)

        return {"data": serializer}, HTTPStatus.OK

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        parse = reqparse.RequestParser()
        parse.add_argument("sort_numbers", type=str, required=True)
        kwargs = parse.parse_args()


        UserModel.query.get_or_404(user_id)


        if int(kwargs.sort_numbers) <6 or int(kwargs.sort_numbers)>10 :
            return {
                "message": "invalid sort number, valid number range is 6 to 10"
            }, HTTPStatus.BAD_REQUEST

        mega_result, phrase_result = get_ms_result()
        if not mega_result:
            return {
                "message": "Could not perform the operation, please try again."
            },HTTPStatus.CONFLICT
        kwargs.user_id = user_id
        kwargs.sorted_numbers = game_maker(int(kwargs.sort_numbers))
        kwargs.mega_result = mega_result

        kwargs.correct_numbers = compare_string(kwargs.mega_result, kwargs.sorted_numbers)
        kwargs.result_sort = message_result(phrase_result)
        new_game = GameModel(**kwargs)
        db_manager(new_game)
        serializer = game_schema.dump(new_game)


        return {"data": serializer}, HTTPStatus.CREATED

   

