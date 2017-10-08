from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    return 'Fitness Tracker!'


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
