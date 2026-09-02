from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from opr_battler.constants.mocks import armies
from opr_battler.get_armies import get_armies
from opr_battler.helpers.handle_armies import handle_armies

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    icon_down = Path("static/icons/arrow-down.svg")

    if not icon_down.is_file():
        print("not a file")
    handled_armies = handle_armies(armies)
    return templates.TemplateResponse(
        request, "home.html", {"armies": handled_armies, "icon_down": icon_down}
    )


@app.get("/get_armies", name="get_armies")
def army_list():
    """
    Call get armies and returns list of armies for Grimdark Future from OPR page
    """
    r = get_armies()

    return r
