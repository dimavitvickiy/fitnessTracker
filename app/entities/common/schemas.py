from marshmallow import fields, Schema


class BaseSchema(Schema):
    id = fields.Integer()
