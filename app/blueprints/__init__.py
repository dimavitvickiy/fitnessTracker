from flask import Blueprint


def set_up_user_views(app):
    from app.entities.user.views import UserList

    user = Blueprint('user', app, url_prefix='user')
    user.add_url_rule(
        '/list',
        UserList.as_view('user_list'),
    )
