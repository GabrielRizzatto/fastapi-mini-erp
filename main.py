from fastapi import FastAPI
from routers.auth_router import auth_router
from database import engine, Base
from models import user

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)