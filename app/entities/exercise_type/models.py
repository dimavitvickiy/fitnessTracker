from app import db
from app.entities.common.models import BaseModel


class ExerciseType(BaseModel):
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
