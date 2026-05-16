import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserSchema
from schemas.login_schema import LoginSchema
from security import bcrypt_context, create_access_token
from repositories.user_repository import save_user, get_user_by_email 

def create_user_service(usuario_schema: UserSchema, session: Session):
    user = get_user_by_email(usuario_schema.email, session)

    if user:        
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    else:
        hashed_password = bcrypt_context.hash(usuario_schema.password)
        
        new_user = User(
        name= usuario_schema.name,
        email = usuario_schema.email,
        password = hashed_password,
        is_active = usuario_schema.is_active,
        is_admin = usuario_schema.is_admin
     )
        
        return save_user(new_user, session)
    
def login_service(login_schema : LoginSchema, session : Session):
    user = get_user_by_email(login_schema.email, session)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    
    elif not bcrypt_context.verify(login_schema.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    
    else:
        access_token = create_access_token(user.id)

    return {"access_token" : access_token,
            "token_type" : "Bearer"}