from flask import jsonify
from flask.views import MethodView

from app.entities.user.models import User


class UserList(MethodView):
    def get(self):
        users = User.query.all()
        return jsonify(users)
