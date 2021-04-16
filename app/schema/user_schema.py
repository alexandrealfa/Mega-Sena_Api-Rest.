from . import UserModel, ma


class UserSchema(ma.Schema):
    class Meta:
        model = UserModel

    id = ma.String()
    name = ma.String()
    phone = ma.String()
    email = ma.String()
    profile_picture = ma.String()


user_schema = UserSchema()
users_schema = UserSchema(many=True)
