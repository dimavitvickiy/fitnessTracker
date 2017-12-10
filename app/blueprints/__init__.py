from flask import Blueprint


def set_up_user_views(app, url_prefix):
    from app.entities.user.views import UserList
    from app.entities.user.views import UserLogin
    from app.entities.user.views import UserLogout

    user_blueprint = Blueprint('user', __name__)
    user_blueprint.add_url_rule(
        '/list',
        view_func=UserList.as_view('user_list'),
    )

    user_blueprint.add_url_rule(
        '/login',
        view_func=UserLogin.as_view('UserLogin'),
    )

    user_blueprint.add_url_rule(
        '/login',
        view_func=UserLogout.as_view('UserLogout'),
    )

    app.register_blueprint(user_blueprint, url_prefix=url_prefix)
