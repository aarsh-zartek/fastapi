from fastapi import HTTPException, status
from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class CredentialsException(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    ) -> None:
        super().__init__(
            status_code,
            detail,
            headers,
        )


class Hash:
    def encrypt(self, pwd: str) -> str:
        return context.hash(secret=pwd)

    def verify(self, password, hashed_password) -> bool:
        return context.verify(password, hashed_password)
