from typing import Optional
from pydantic import BaseModel


class CDSServicesDiscoveryItem(BaseModel):
    hook: str
    title: str
    description: str
    id: str
