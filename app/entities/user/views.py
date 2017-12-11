import hashlib

from flask import jsonify, request, redirect
from flask.views import MethodView
from flask_login import login_user, logout_user

from app import db
from app.entities.user.models import User
from app.entities.user.schemas import UserSchema
from app.helpers.password import generate_password


class UserList(MethodView):
    def get(self):
        # get all users from db
        users = User.query.all()
        # dump users to convert into json
        dumped_users = UserSchema().dump(users, many=True).data

        return jsonify(dumped_users)

    def post(self):
        data, errors = UserSchema().load(request.json)
        if errors:
            return jsonify(errors), 400

        is_user_exist = User.query.filter_by(
            username=data.get('username')
        ).all()

        if is_user_exist:
            return jsonify({'errors': 'Username already exist'})

        user = User(
            username=data.get('username'),
            password=generate_password(data.get('password')),
        )
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return jsonify({})


class UserLogin(MethodView):
    def post(self):
        data, errors = UserSchema().load(request.json)
        if errors:
            return jsonify(errors), 400

        user = User.query.filter_by(
            username=data.get('username'),
            password=generate_password(data.get('password')),
        ).one_or_none()

        if user:
            login_user(user)
            return jsonify({})
        return jsonify({'error': 'User does not exist or password is wrong'}), 400


class UserLogout(MethodView):
    def get(self):
        logout_user()
        return redirect('/')
