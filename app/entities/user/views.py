from flask import jsonify, request
from flask.views import MethodView
from flask_login import login_user

from app.entities.user.models import User
from app.entities.user.schemas import UserSchema


class UserList(MethodView):
    def get(self):
        # get all users from db
        users = User.query.all()
        # dump users to convert into json
        dumped_users = UserSchema().dump(users, many=True).data

        return jsonify(dumped_users)


class UserLogin(MethodView):
    def post(self):
        data, errors = UserSchema().load(request.json)
        print(errors)
        if errors:
            return jsonify(errors), 400

        user = User.query.filter_by(
            username=data.get('username'),
            password=data.get('password'),
        ).one_or_none()

        if user:
            login_user(user)
            return jsonify({})
        return jsonify({'error': 'User does not exist'}), 400
