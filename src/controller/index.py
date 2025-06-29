from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.config.path import path_dir

router = APIRouter()
template = Jinja2Templates(directory=path_dir["template"])


@router.get(
    path="/",
    response_class=HTMLResponse,
    include_in_schema=False
)
async def method(request: Request):
    result = {
        "page": "page/index.html",
        "code": 200,
        "context": {
            "request": request,
            "a": None,
            "b": None,
            "c": None,
        }
    }
    return template.TemplateResponse(
        name=result["page"],
        context=result["context"],
        status_code=200
    )
