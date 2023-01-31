from datetime import datetime, timedelta

from jose import JWTError, jwt

from app.schemas import TokenData
from app.utils import CredentialsException


SECRET_KEY = "86d0271841b044e2a9a88f430fefae31d0e32ad411d744c887dbb32d8fb560d3"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise CredentialsException()
        token_data = TokenData(email=email)
        return token_data
    except JWTError as err:
        raise CredentialsException() from err
