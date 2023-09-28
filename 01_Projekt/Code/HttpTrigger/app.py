from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from scraper import get_website_info
from date_calc import get_creation_date_info
from web_scraper_urlhaus import web_scraper_urlhaus
from urllib.parse import unquote
from fastapi.responses import RedirectResponse
from web_scraper_urlhaus import web_scraper_urlhaus
from routers import router_root



app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def page_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/news")
async def page_news(request: Request):
    return templates.TemplateResponse("news.html", {"request": request})


@app.get("/contact")
async def page_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/about")
async def page_about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("about.html", context)


@app.get("/melden")
async def page_about(request: Request):
    return templates.TemplateResponse("melden.html", {"request": request})
