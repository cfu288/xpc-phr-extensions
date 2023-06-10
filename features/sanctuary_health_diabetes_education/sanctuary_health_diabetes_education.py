from fastapi import Response
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import urllib
from features.sanctuary_health_diabetes_education.models.SanctuaryHealthDiabetesEducationRequest import (
    SanctuaryHealthDiabetesEducationRequest,
)
from python_graphql_client import GraphqlClient
import time

# fmt: off
query = gql('''
query{
  getPosts(sequelizeQuery: {
    where: "{ \\"id\\": \\"87213d39-a005-494d-a1df-05f1daaeae11\\"}"
  }){
    id
    title
    topic
    description
    icd10
    approximateTime
    mediaFileDetailsList {
      file{
        filename
        url
        updatedAt
      }
    }
  }
}
''')

transport = AIOHTTPTransport(url="https://v4-0-dot-livitay.appspot.com/graphql", headers={"apikey": "3ba6d6af-e690-444c-a902-aebff6c41384"})


class SanctuaryHealthDiabetesEducationHandler:
    def __init__(self):
        self.client = Client(transport=transport, fetch_schema_from_transport=True)

    def handle(self, req: SanctuaryHealthDiabetesEducationRequest) -> Response:
        # in reality, we would use the req with the users fhirSources.fhirServer, fhirSources.fhirAuthorization
        # and context.diagnosticReportId to query for the relevant diagnostic report data, see if any of the data contains
        # an A1C value, and if so, return the appropriate response. Otherwise, return an empty response.
        # For now, we will just return a static response since our test patients in the Epic sandbox don't have useful A1C values.

        # Since we don't have real data to work with, we'll pseudocode the patient data fetching process here without the actual code.:
        fhirServices = req.fhirServices
        for fhirService in fhirServices:
            # make a get request to the fhirService.fhirServer with the fhirService.fhirAuthorization
            # and context.diagnosticReportId to get the diagnostic report data
            url = fhirService.fhirServer + "/DiagnosticReport?"
            params = {'id': req.contexts.get(fhirService.fhirServer).diagnosticReportId}
            print("Making a request to the following patient url:" + url +  urllib.parse.urlencode(params) + " with access token " + fhirService.fhirAuthorization.accessToken)


        result = self.client.execute(query)
         # Fake patient data, use this
        if req.contexts.get(fhirService.fhirServer).diagnosticReportId in set(
            ["TeOs2UvPrb0X2j3quRbvpAnIv8HVpc3MfPHsTs5MXbxQB"]
        ):
          return [
              {
                  "summary": "Patient Education - " + result.get("getPosts")[0].get("title"),
                  "detail": result.get("getPosts")[0].get("description"),
                  "indicator": "info",
                  "source": {"label": "Sanctuary Health", "url": "https://docs.sanctuaryhealth.io/", "icon": "https://app.sanctuaryhealth.io/static/media/SanctuaryLogo.aefca1806c2c652b26b79c29e6993e1d.svg"},
                  "links": [
                      {
                          "label": "Video",
                          "url": result.get("getPosts")[0].get("mediaFileDetailsList")[0].get("file").get("url"),
                          "type": "absolute",
                      }
                  ],
              }
          ]
        return []
