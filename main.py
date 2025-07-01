from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from src.api.routes import routes as api_routes
from src.config.path import path_dir
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
# context = {
#     "request": None,
#     "code": 0,
#     "msg": None,
# }


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    # global context
    # context["request"] = request,
    # context["code"] = exc.status_code,
    # context["msg"] = f"Page {exc.detail}"
    context = {
        "request": request,
        "code": exc.status_code,
        "msg": None
    }

    if context["code"] == 404:
        context["msg"] = f"Page {exc.detail}"
        return template.TemplateResponse(
            name="page/error.html",
            context=context,
            status_code=context["code"]
        )


@app.exception_handler(Exception)
async def internal_error_handler(request: Request, exc: Exception):
    print(f"\nError : {exc}\n")
    context = {
        "request": request,
        "code": 500,
        "msg": None
    }
    return template.TemplateResponse(
        name="page/error.html",
        context=context,
        status_code=context["code"]
    )

for route in controller_routes:
    app.include_router(route)
for route in api_routes:
    app.include_router(route)
