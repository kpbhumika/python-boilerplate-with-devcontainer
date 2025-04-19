# -----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
# -----------------------------------------------------------------------------------------

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from api.endpoint import api_router



home_router = APIRouter()


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@home_router.get("/health")
async def health():
    return {"status": "ok"}


@home_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def run_setup():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.mount("/templates", StaticFiles(directory="templates"), name="static")
    app.include_router(home_router, prefix="", tags=["home"])
    app.include_router(api_router, prefix="/api", tags=["api"])

run_setup()