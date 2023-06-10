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
            ]
        }
