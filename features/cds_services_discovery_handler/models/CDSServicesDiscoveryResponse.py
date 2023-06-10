from pydantic import BaseModel

from features.cds_services_discovery_handler.models.CDSServicesDiscoveryItem import (
    CDSServicesDiscoveryItem,
)


class CDSServicesDiscoveryResponse(BaseModel):
    services: list[CDSServicesDiscoveryItem]
