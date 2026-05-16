import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_session
from schemas.user_schema import UserSchema
from schemas.login_schema import LoginSchema
from models.user import User
from services.auth_service import create_user_service, login_service, refresh_token_service  
from security import get_current_user

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/create-user")
async def create_user(usuario_schema: UserSchema, session : Session = Depends(get_session)):
   
    new_user = create_user_service(usuario_schema, session)

    return {"message": "User created successfully", "email": new_user.email}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session : Session = Depends(get_session)):
    return login_service(login_schema, session)

@auth_router.post("/refresh")
async def refresh_token(user: User = Depends(get_current_user)):
    return refresh_token_service()