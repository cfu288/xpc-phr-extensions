from typing import Literal
from pydantic import BaseModel


class ContextsItem(BaseModel):
    patientId: str
    diagnosticReportId: str


class FhirAuthorizationItem(BaseModel):
    accessToken: str
    tokenType: str
    expiresIn: int
    scope: str
    subject: str


class FhirServicesItem(BaseModel):
    fhirServer: str
    fhirAuthorization: FhirAuthorizationItem


class SanctuaryHealthDiabetesEducationRequest(BaseModel):
    hookInstance: str
    hook: Literal["diagnostic-report-open"]
    fhirServices: list[FhirServicesItem]
    contexts: dict[str, ContextsItem]
