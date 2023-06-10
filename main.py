import os
from dotenv import load_dotenv

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
from features.diabetes_ai_advisor.diabetes_ai_advisor_handler import (
    DiabetesAIAdvisorHandler,
)

from features.root.root_handler import RootHandler
from features.sanctuary_health_diabetes_education.models.SanctuaryHealthDiabetesEducationRequest import (
    SanctuaryHealthDiabetesEducationRequest,
)
from features.sanctuary_health_diabetes_education.sanctuary_health_diabetes_education import (
    SanctuaryHealthDiabetesEducationHandler,
)

load_dotenv()
is_development = os.getenv("ENVIRONMENT") == "development"
rp = "" if is_development else "/kps-ivs-rkf"
print(is_development)

app = FastAPI(root_path="/kps-ivs-rkf")
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
    return SanctuaryHealthDiabetesEducationHandler().handle(body)


@app.post(
    "/cds-services/diabetes-ai-advisor",
    # response_model=SanctuaryHealthDiabetesEducationResponse,
    response_model_exclude_none=True,
    tags=["hooks"],
)
def cds_services_discovery(body: SanctuaryHealthDiabetesEducationRequest):
    return DiabetesAIAdvisorHandler().handle(body)
