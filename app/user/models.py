from manage import db


class User(db.Model):
    username = db.String(nullable=False)
    password = db.String(nullable=False)
