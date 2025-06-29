from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import jwt

from src.config.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


async def generate_token(data: dict):
    expiration = datetime.now(ZoneInfo("Asia/Jakarta")) + \
        timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))
    data.update({"exp": expiration})
    return {
        "x-access-token": jwt.encode(payload=data, key=SECRET_KEY, algorithm=ALGORITHM),
        "expired": str(expiration)[:26],
    }
