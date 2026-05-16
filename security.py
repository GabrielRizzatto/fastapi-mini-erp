from passlib.context import CryptContext
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta, timezone
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def create_access_token(user_id):
    expires_at = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    token_payload = {"sub": str (user_id), "exp": expires_at}
    jwt_token = jwt.encode(token_payload, SECRET_KEY, ALGORITHM)

    return jwt_token