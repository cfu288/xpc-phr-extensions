from pydantic import BaseModel

from models.CDSCard import CDSCard


class CDSCardsResponse(BaseModel):
    cards: list[CDSCard]
