from typing import Literal, Optional
from pydantic import BaseModel


class CDSHookRequestBodyFHIRServicesAuthorization(BaseModel):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    scope: str
    subject: str


class CDSHookRequestBodyFHIRServices(BaseModel):
    fhirServer: str
    fhirAuthorization: CDSHookRequestBodyFHIRServicesAuthorization


class CDSHookRequest(BaseModel):
    hookInstance: str
    hook: Literal["app-start"] | Literal["diagnostic-report-open"]
    fhirServices: Optional[list[CDSHookRequestBodyFHIRServices]]
    context: Optional[dict]
    contexts: Optional[dict]
    prefetch: Optional[dict]
