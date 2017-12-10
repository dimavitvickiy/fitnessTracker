from flask_login import UserMixin as LoginUserMixin

from app import db
from app.entities.common.models import BaseModel


class User(LoginUserMixin, BaseModel):
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
