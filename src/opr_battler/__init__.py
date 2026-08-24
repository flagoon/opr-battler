from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from opr_battler.army_book import ArmyBook
from opr_battler.constants.mocks import armies
from opr_battler.get_armies import get_armies

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory="templates")


def handle_armies(armies: list[ArmyBook]):
    # find all armies that are specific faction (blood angles, ultramarines -> blood brothers, etc)
    new_armies: dict[str, ArmyBook] = {}
    for army in armies:
        if army["factionId"] is None:
            if not army["coverImagePath"].startswith("https"):
                army["coverImagePath"] = (
                    "https://army-forge.opr-cdn.com/" + army["coverImagePath"]
                )
            new_armies[army.get("uid")] = army
        else:
            if new_armies.get("factionId") is None:
                # find parent army
                parent_army = next(
                    (a for a in armies if army.get("uid") == army["factionId"]), None
                )
                if parent_army is not None:
                    new_armies[parent_army["uid"]] = parent_army

    return new_armies


@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    handled_armies = handle_armies(armies)
    return templates.TemplateResponse(request, "home.html", {"armies": handled_armies})


@app.get("/get_armies", name="get_armies")
def army_list():
    """
    Call get armies and returns list of armies for Grimdark Future from OPR page
    """
    r = get_armies()

    return r
