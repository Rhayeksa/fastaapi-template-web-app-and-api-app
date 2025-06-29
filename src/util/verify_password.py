from passlib.context import CryptContext


async def verify_password(password: str, hashed_password: str):
    return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(secret=password, hash=hashed_password)
