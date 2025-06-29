from fastapi import APIRouter
from fastapi.responses import FileResponse

from src.config.path import path_dir

router = APIRouter()


@router.get("/favicon.ico", include_in_schema=False)
async def method():
    return FileResponse(path_dir["static"] / "favicon/favicon.ico")
