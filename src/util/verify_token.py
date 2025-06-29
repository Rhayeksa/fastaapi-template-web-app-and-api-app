import jwt

from src.config.jwt import ALGORITHM, SECRET_KEY


async def verify_token(token: str):
    try:
        return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return False