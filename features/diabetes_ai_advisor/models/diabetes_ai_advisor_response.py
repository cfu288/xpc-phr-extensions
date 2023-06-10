from pydantic import BaseModel
from models.CDSCard import CDSCard


class DiabetesAIAdvisorResponse(BaseModel):
    __root__: list[CDSCard]
