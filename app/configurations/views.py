from flask import Flask
from flask_restful import Api


def init_app(app: Flask):
    api = Api(app)

    from app.views.access_view import SignIn
    from app.views.games_view import AllGamers, Games
    from app.views.user_view import AllUser, User

    api.add_resource(User, "/user", endpoint="/user", methods=["POST", "GET", "PATCH", "DELETE"])
    api.add_resource(AllGamers, "/games", endpoint="/games", methods=["GET"])
    api.add_resource(Games, "/game", endpoint="/game", methods=["GET", "POST"])
    api.add_resource(SignIn, "/sigin", endpoint="/sigin", methods=["POST"])