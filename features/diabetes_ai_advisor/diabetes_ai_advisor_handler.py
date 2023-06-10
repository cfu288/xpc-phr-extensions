from fastapi import Response
import urllib
from features.diabetes_ai_advisor.models.diabetes_ai_advisor_request import (
    DiabetesAIAdvisorRequest,
)
import time


class DiabetesAIAdvisorHandler:
    def __init__(self):
        pass

    def handle(self, req: DiabetesAIAdvisorRequest) -> Response:
        print(req)
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
            params = {"id": req.contexts.get(fhirService.fhirServer).diagnosticReportId}
            print(
                "Making a request to the following patient url:"
                + url
                + urllib.parse.urlencode(params)
                + " with access token "
                + fhirService.fhirAuthorization.accessToken
            )

        # Fake patient data, use this
        if req.contexts.get(fhirService.fhirServer).diagnosticReportId in set(
            ["TeOs2UvPrb0X2j3quRbvpAnIv8HVpc3MfPHsTs5MXbxQB"]
        ):
            time.sleep(2)
            return [
                {
                    "summary": "Diabetes AI Advisor - Powered by OpenAI",
                    "detail": """Your A1c values have been increasing over the years, indicating a slight decline in blood sugar control. A higher A1c means poorer blood sugar control. You should:
                    <ul>
                        <li> - Monitor blood sugar levels regularly.</li>
                        <li> - Review your diabetes management plan and make adjustments if necessary.</li>
                        <li> - Focus on healthy lifestyle habits like balanced eating, exercise, sleep, stress management, and maintaining a healthy weight.</li>
                    </ul>
                    </br>
                    <div style="border-bottom: 1px solid #000;"></div>
                    </br>
                    <b>Below are the resources available to you:</b>
                    </br>
                    <b>Virta Health</b> - a digital solution to reverses type 2 diabetes and pre-diabetes. <a style="color:blue" href="https://www.virtahealth.com/">Learn more</a>
                    </br>
                    <b>Livongo</b> - smart management of diabetes with personalized tips and expert coaching. <a style="color:blue" href="https://www.virtahealth.com/">Learn more</a>
                    """,
                    "indicator": "info",
                    "source": {
                        "label": "Diabetes AI Advisor",
                        "url": "https://openai.com/",
                        "icon": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg",
                    },
                    "links": [
                        # {
                        #     "label": "Virta Health - Schedule a zero dollar enrollment consultation to learn more",
                        #     "url": "www.example.com",
                        #     "type": "absolute",
                        # },
                        # {
                        #     "label": "Virta Health - Schedule a zero dollar enrollment consultation to learn more",
                        #     "url": "www.example.com",
                        #     "type": "absolute",
                        # },
                    ],
                }
            ]

        return []
