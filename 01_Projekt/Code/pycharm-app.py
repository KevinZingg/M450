#  Copyright Siemens AG, 2023 - 2023
#  Licensed under the Siemens Inner Source License, see LICENSE
import os
from datetime import datetime
from fastapi import FastAPI, Request, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from routers import router_root
from siep39 import dot_env

dot_env.load_sie_env(debug=False)
# f 'api://{os.environ.get("APP_CLIENT_ID")}/user_impersonation': 'user_impersonation',
azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=os.environ.get("APP_CLIENT_ID"),
    tenant_id=os.environ.get("TENANT_ID"),
    scopes={f'api://{os.environ.get("APP_CLIENT_ID")}/user_impersonation': 'user_impersonation'}
)
app = FastAPI(swagger_ui_oauth2_redirect_url='/oauth2-redirect',
              swagger_ui_init_oauth={
                  'usePkceWithAuthorizationCodeGrant': True,
                  'clientId': os.environ.get("OPENAPI_CLIENT_ID"),
              })
app.add_middleware(CORSMiddleware,
                   allow_origins=[str(origin) for origin in 'http://localhost:8000'],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'],
                   )
app.mount('/static', StaticFiles(directory='static'), name='static')
app.include_router(router_root.router)
# app.include_router(api_router, prefix=settings.API_V1_STR,
# dependencies=[Security(azure_scheme, scopes=['user_impersonation'])])


@app.on_event("startup")
async def op_startup():
    print(f'** Startup event FastAPI v {datetime.now().strftime("%y.%j")}')
    await azure_scheme.openid_config.load_config()
    print(f' startup done')


# Security(azure_scheme, scopes=['user_impersonation'])
# , user: User = Security(azure_scheme, scopes=['user_impersonation'])
@app.get("/news", dependencies=[Security(azure_scheme)])
async def page_news(request: Request):
    print(f' user request: request.state.user.dict()')
    return 'Hello news'
