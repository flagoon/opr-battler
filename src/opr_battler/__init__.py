from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from opr_battler.get_armies import get_armies

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"data": "zupa"})


@app.get("/zupa", include_in_schema=False)
def zupa(request: Request):
    return templates.TemplateResponse(request, "zupa.html", {"title": "mamurki"})


@app.get("/get_armies")
def army_list():
    r = get_armies()

    return r.content
