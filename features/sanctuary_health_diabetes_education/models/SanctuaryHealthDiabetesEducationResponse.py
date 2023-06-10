from pydantic import BaseModel
from models.CDSCard import CDSCard


class SanctuaryHealthDiabetesEducationResponse(BaseModel):
    __root__: list[CDSCard]
