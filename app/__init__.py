import os

from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from app.blueprints import set_up_user_views

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')

app = Flask(
    __name__,
    template_folder=TEMPLATE_FOLDER,
    static_folder=STATIC_FOLDER,
)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
redis = Redis(host='redis', port=6379)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


set_up_user_views(app, url_prefix='/user')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template(
        'index.html.jinja2',
    )

@login_manager.user_loader
def load_user(user_id):
    from app.entities.user.models import User
    return User.query.get(user_id)
