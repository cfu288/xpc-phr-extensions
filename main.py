from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from features.cds_services_discovery_handler.cds_services_discovery_handler import (
    CDSServicesDiscoveryHandler,
)
from features.cds_services_discovery_handler.models.CDSServicesDiscoveryResponse import (
    CDSServicesDiscoveryResponse,
)

from features.root.root_handler import RootHandler
from features.sanctuary_health_diabetes_education.models.SanctuaryHealthDiabetesEducationRequest import (
    SanctuaryHealthDiabetesEducationRequest,
)
from features.sanctuary_health_diabetes_education.sanctuary_health_diabetes_education import (
    SanctuaryHealthDiabetesEducationHandler,
)

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def root():
    return RootHandler().handle()


@app.get(
    "/cds-services",
    response_model=CDSServicesDiscoveryResponse,
    response_model_exclude_none=True,
    tags=["discovery"],
)
def cds_services_discovery():
    return CDSServicesDiscoveryHandler().handle()


@app.post(
    "/cds-services/sanctuary-health-diabetes-education",
    # response_model=SanctuaryHealthDiabetesEducationResponse,
    response_model_exclude_none=True,
    tags=["hooks"],
)
def cds_services_discovery(body: SanctuaryHealthDiabetesEducationRequest):
    print(body)
    return SanctuaryHealthDiabetesEducationHandler().handle(body)
