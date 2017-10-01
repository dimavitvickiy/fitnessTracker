from flask import Flask
app = Flask(__name__)

PROJECT_NAME = "Fitness Tracker"


@app.route("/")
def hello():
    return "Hello {}".format(PROJECT_NAME)
