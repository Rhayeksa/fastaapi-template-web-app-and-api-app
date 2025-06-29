from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.config.path import path_dir
from src.api.routes import routes as api_routes
from src.controller.routes import routes as controller_routes

app = FastAPI(
    # title=PROJECT or "FastAPI",
    # description=DESCRIPTION or "FastAPI",
    # version=VERSION or "0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # Menutup model dengan default
        "defaultModelExpandDepth": -1,  # Menutup model dengan default
        "docExpansion": "none",  # Menutup endpoint
    },
    # docs_url="/docs" if DEBUG else None,
    # openapi_url="/openapi.json" if DEBUG else None,
    # redoc_url="/redoc" if DEBUG else None,
)

app.mount("/static", StaticFiles(directory=path_dir["static"]), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

template = Jinja2Templates(directory=path_dir["template"])


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return template.TemplateResponse("page/error/404.html", {"request": request}, status_code=404)


@app.exception_handler(Exception)
async def internal_error_handler(request: Request, exc: Exception):
    print(f"\nError : {exc}\n")
    return template.TemplateResponse("page/error/500.html", {"request": request}, status_code=500)

for route in controller_routes:
    app.include_router(route)
for route in api_routes:
    app.include_router(route)
