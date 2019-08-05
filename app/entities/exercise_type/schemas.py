from marshmallow import fields
from app.entities.common.schemas import BaseSchema


class ExersiceTypeSchema(BaseSchema):
    name = fields.String()
    description = fields.String()
