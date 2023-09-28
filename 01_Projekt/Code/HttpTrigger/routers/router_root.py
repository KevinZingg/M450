#  Copyright Siemens AG, 2021 - 2023
#  Licensed under the Siemens Inner Source License, see LICENSE
__author__ = 'Daniel Panizza'
__version__ = '23.250'
__maintainer__ = 'Daniel Panizza'
__status__ = 'Development'  # Development | Production

import os

from fastapi import APIRouter, Request, Security, HTTPException, Form, Query
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer

from date_calc import get_creation_date_info
from scraper import get_website_info
from web_scraper_urlhaus import web_scraper_urlhaus
from urllib.parse import unquote, urlparse, quote
from fastapi.responses import RedirectResponse
import sqlite3

# Imports from own files

from constants import DB_PATH
from db_operations import get_bad_sites_from_db
from url_checking import is_domain_safe
from template_rendering import render_template

router = APIRouter(prefix='', tags=['Root'])
router.mount('/static', StaticFiles(directory='static'), name='static')

@router.get("/")
async def page_home(request: Request):
    context = {'message': 'Home'}
    return render_template("home.html", request, context)


@router.get('/favicon.ico', response_class=FileResponse)
async def favicon():
    return FileResponse("static/favicon.ico")


@router.get("/news_old", response_class=HTMLResponse)
async def page_news(request: Request):
    return render_template("news.html", request)


@router.get("/contact", response_class=HTMLResponse)
async def page_contact(request: Request):
    return render_template("contact.html", request)


@router.get("/about", response_class=HTMLResponse)
async def page_about(request: Request):
    return render_template("about.html", request)


@router.get("/melden", response_class=HTMLResponse)
async def page_about(request: Request):
    return render_template("melden.html", request)


@router.post("/handle-search")
async def handle_search(request: Request, domain: str = Form(...)):
    if is_domain_safe(domain):
        parsed_domain = urlparse(domain)
        if not parsed_domain.netloc:
            parsed_domain = urlparse('http://' + domain)
        domain_name = parsed_domain.netloc
        return {"redirect": f"/whois/{domain_name}"}
    else:
        encoded_domain = quote(domain)
        return {"redirect": f"/url_haus?domain={encoded_domain}"}


scraper = web_scraper_urlhaus()
bad_sites = scraper.get_all_urls()

@router.get("/check-url")
def check_url(full_url: str):
    safety_status = "yes" if is_domain_safe(full_url) else "no"
    return {"is_safe": safety_status}


@router.get("/urlhaus")
def urlhaus(request: Request):
    return render_template("url_haus.html", request, {"bad_sites": bad_sites})


@router.get("/whois/{domain}", response_class=HTMLResponse)
async def get_whois(request: Request, domain: str):
    try:
        w = get_website_info(domain)
        creation_date_color, creation_date_text, creation_date_expl = get_creation_date_info(w)
        context = {
            "domain": domain,
            "w": w,
            "creation_date_color": creation_date_color,
            "creation_date_text": creation_date_text,
            "creation_date_expl": creation_date_expl
        }
        return render_template("whois.html", request, context)
    except Exception as e:
        return render_template("error.html", request, {"error": str(e)})

@router.get("/suspicious", response_class=HTMLResponse)
async def page_about(request: Request):
    return render_template("suspicious.html", request)


@router.get("/url_haus", response_class=HTMLResponse)
async def get_url_haus(request: Request, domain: str = Query(...)):
    decoded_domain = unquote(domain)
    try:
        url_haus_domains = scraper.get_all_urls()
        if decoded_domain in url_haus_domains:
            return render_template("url_haus.html", request, {"domain": decoded_domain})
        else:
            return RedirectResponse(url=f"/whois/{decoded_domain}")
    except Exception as e:
        return render_template("error.html", request, {"error": str(e)})