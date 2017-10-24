from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

from app.blueprints import set_up_user_views

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
redis = Redis(host='redis', port=6379)
migrate = Migrate(app, db)

set_up_user_views(app)
