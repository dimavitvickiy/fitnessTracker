from app.entities.common.schemas import BaseSchema
from marshmallow import fields


class LessonSchema(BaseSchema):
    startTime = fields.DateTime
    endTime = fields.DateTime
    isApprovedByClient = fields.Boolean
