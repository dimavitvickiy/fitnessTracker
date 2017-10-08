from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import Redis

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return 'Fitness Tracker! !!!'


if __name__ == "__main__":
    app.run()
