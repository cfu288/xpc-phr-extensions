from typing import Optional
from pydantic import BaseModel


class CDSCardSource(BaseModel):
    label: str
    url: Optional[str]
    icon: Optional[str]


class CDSCardAction(BaseModel):
    type: str
    description: str
    resource: Optional[dict]


class CDSCardSuggestion(BaseModel):
    label: str
    uuid: Optional[str]
    actions: Optional[list[CDSCardAction]]


class CDSCardLink(BaseModel):
    label: str
    url: str
    type: str


class CDSCard(BaseModel):
    """
    https://cds-hooks.hl7.org/1.0/#card-attributes
    """

    summary: str
    detail: Optional[str]
    indicator: str
    source: CDSCardSource
    links: Optional[list[CDSCardLink]]
