from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from opr_battler.army_book import map_all_armies
from opr_battler.constants.mocks import armies
from opr_battler.get_armies import get_armies

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False, name="home")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"armies": armies})


@app.get("/get_armies", name="get_armies")
def army_list():
    """
    Call get armies and returns list of armies for Grimdark Future from OPR page
    """
    r = get_armies()
    mapped_armies = list(map_all_armies(r))

    with open("src/opr_battler/files/example.csv", "w") as file:
        file.writelines(
            f"{army['uid']}; {army['name']}; {army['desc']}; {army['cover_image']}\n"
            for army in mapped_armies
        )
    return mapped_armies
