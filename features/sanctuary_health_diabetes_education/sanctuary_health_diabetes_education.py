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
          [
            "TeOs2UvPrb0X2j3quRbvpAnIv8HVpc3MfPHsTs5MXbxQB",
            "TP2hYGwg-.5LFT84WduGn8qWmQp80d66Br.bZT.okcu4B",
            "TgnIbHY714d5JDcg.iIiVQKhJHnxeIO4rrV03bq1W5VQB1",
            "T8A7CSOhucBPc2wJxlHlS4gB",
            "TgnIbHY714d5JDcg.iIiVQKhJHnxeIO4rrV03bq1W5VQB"
          ]
        ):
          return [
              {
                  "summary": "Patient Education - " + result.get("getPosts")[0].get("title"),
                  "detail": result.get("getPosts")[0].get("description"),
                  "indicator": "info",
                  "source": {"label": "Sanctuary Health", "url": "https://docs.sanctuaryhealth.io/", "icon": "https://app.sanctuaryhealth.io/static/media/SanctuaryLogo.aefca1806c2c652b26b79c29e6993e1d.svg"},
                  "links": [
                      {
                          "label": "Watch our video",
                          "url": result.get("getPosts")[0].get("mediaFileDetailsList")[0].get("file").get("url"),
                          "type": "absolute",
                      },
                          {
                          "label": "Subscribe to our platform",
                          "url": "https://app.sanctuaryhealth.io/",
                          "type": "absolute",
                      }
                  ],
              },
              {
                  "summary": "Find a nutritionist",
                  "detail": "Personalized, virtual nutrition care from experts you cantrust. Covered by your insurance (really).",
                  "indicator": "info",
                  "source": {"label": "Culina Health", "url": "https://culinahealth.com/", "icon": "https://files.mari.casa/culina.webp"},
                  "links": [
                      {
                          "label": "Schedule a free call",
                          "url": "https://culinahealth.com/",
                          "type": "absolute",
                      },
                  ],
              },
                {
                  "summary": "Schedule your next appointment with Dr. Smith",
                  "detail": "Here are some available appointments this upcoming week. Click one of the buttons below to create an appointment, we'll transfer your registration data automatically so you can skip the forms at the front desk.",
                  "indicator": "info",
                  "source": {"label": "Flight Health", "url": "https://goflighthealth.com/", "icon": "https://files.mari.casa/flight-health.jpeg"},
                  "links": [
                      {
                          "label": "Tuesday, 10:00 am",
                          "url": "https://www.goflighthealth.com/",
                          "type": "absolute",
                      },
                         {
                          "label": "Tuesday, 11:00 am",
                          "url": "https://www.goflighthealth.com/",
                          "type": "absolute",
                      },
                            {
                          "label": "Tuesday, 12:00 pm",
                          "url": "https://www.goflighthealth.com/",
                          "type": "absolute",
                      },
                  ],
              }
          ]
        return []
