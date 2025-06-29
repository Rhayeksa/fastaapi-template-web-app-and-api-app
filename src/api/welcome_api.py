from fastapi import APIRouter
from src.util.response import response

router = APIRouter()


@router.get(path="/api", name="Welcome API")
async def welcome_api():
    try:
        return await response(code=200, message="Welcome to API King Ichsan")
    except Exception as e:
        print(f"\nError : {e}\n")
        return await response(code=500)
