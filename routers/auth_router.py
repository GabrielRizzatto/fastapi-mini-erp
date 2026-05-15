import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_session
from schemas.user_schema import UserSchema
from services.auth_service import create_user_service

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/create-user")
async def create_user(usuario_schema: UserSchema, session : Session = Depends(get_session)):
   
    new_user = create_user_service(usuario_schema, session)

    return {"message": "User created successfully", "email": new_user.email}

    