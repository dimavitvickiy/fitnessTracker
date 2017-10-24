from marshmallow import fields

from app.entities.common.schemas import BaseSchema


class UserSchema(BaseSchema):
    username = fields.String()
    password = fields.String()
