from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from app.blueprints import set_up_user_views

app = Flask(__name__)
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)
redis = Redis(host='redis', port=6379)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


set_up_user_views(app, url_prefix='/user')
