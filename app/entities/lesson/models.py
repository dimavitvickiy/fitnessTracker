from app.entities.common.models import BaseModel
from app import db


class Lesson(BaseModel):
    startTime = db.Column(db.DateTime, nullable=False)
    endTime = db.Column(db.DateTime, nullable=False)
    isApprovedByClient = db.Column(db.Boolean, nullable=False)
