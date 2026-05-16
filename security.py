from passlib.context import CryptContext
from dotenv import load_dotenv
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from database import get_session
from repositories.user_repository import get_user_by_id
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def create_access_token(user_id):
    expires_at = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    token_payload = {"sub": str (user_id), "exp": expires_at}
    jwt_token = jwt.encode(token_payload, SECRET_KEY, ALGORITHM)

    return jwt_token

def create_refresh_token(user_id):
    expires_at = datetime.now(timezone.utc) + timedelta(days = REFRESH_TOKEN_EXPIRE_DAYS)
    token_payload = {"sub": str (user_id), "exp": expires_at}
    jwt_token = jwt.encode(token_payload, SECRET_KEY, ALGORITHM)

    return jwt_token


def get_current_user(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM )
        user_id = payload.get("sub")
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_id(int(user_id),session)
    if user_id is None:
            raise credentials_exception
    
    if not user or not user.is_active:
        raise credentials_exception
    
    return user

