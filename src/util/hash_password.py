from passlib.context import CryptContext


async def hash_password(password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(secret=password)
