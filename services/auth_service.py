import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserSchema
from security import bcrypt_context 

def create_user_service(usuario_schema: UserSchema, session: Session):
    user = session.query(User).filter(usuario_schema.email == User.email).first()

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    else:
        password = bcrypt_context.hash(usuario_schema.password)
        
        new_user = User(
        name=usuario_schema.name,
        email=usuario_schema.email,
        password=password,
        is_active = usuario_schema.is_active,
        is_admin = usuario_schema.is_admin
     )
        
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user