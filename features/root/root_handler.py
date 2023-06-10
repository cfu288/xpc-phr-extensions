from fastapi.responses import HTMLResponse, Response


class RootHandler:
    def __init__(self):
        HTMLFile = open("./index.html", "r")
        self.index = HTMLFile.read()

    def handle(self) -> Response:
        html_content = self.index
        return HTMLResponse(content=html_content, status_code=200)
