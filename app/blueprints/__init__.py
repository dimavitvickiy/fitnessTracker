from flask import Blueprint


def set_up_user_views(app, url_prefix):
    from app.entities.user.views import UserList

    user_blueprint = Blueprint('user', __name__)
    user_blueprint.add_url_rule(
        '/list',
        view_func=UserList.as_view('user_list'),
    )

    app.register_blueprint(user_blueprint, url_prefix=url_prefix)
