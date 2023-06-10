class CDSServicesDiscoveryHandler:
    def handle(self):
        return {
            "services": [
                {
                    "hook": "diagnostic-report-open",
                    "title": "Diabetes Education",
                    "description": "Checks your recent A1C and provides education resources via Sanctuary Health",
                    "id": "sanctuary-health-diabetes-education",
                },
                {
                    "hook": "diagnostic-report-open",
                    "title": "Diabetes AI Advisor - Powered by OpenAI",
                    "description": "Have ChatGPT give you insights about your A1C values",
                    "id": "diabetes-ai-advisor",
                },
            ]
        }
