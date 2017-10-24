from flask import jsonify
from flask.views import MethodView

from app.entities.user.models import User
from app.entities.user.schemas import UserSchema


class UserList(MethodView):
    def get(self):
        # get all users from db
        users = User.query.all()
        # dump users to convert into json
        dumped_users = UserSchema().dump(users, many=True).data

        return jsonify(dumped_users)
