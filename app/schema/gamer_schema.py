from app.models.gamer_model import GameModel

from . import ma


class GamerSchema(ma.Schema):
    class Meta:
        model = GameModel
    id = ma.String()
    sort_numbers = ma.String()
    user_id = ma.Integer()
    sorted_numbers = ma.String()
    mega_result = ma.String()
    correct_numbers = ma.String()
    result_sort = ma.String()
    create_at = ma.String()


games_schema = GamerSchema(many=True)
game_schema = GamerSchema()