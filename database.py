import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base = declarative_base()

def get_session():
    try:
        Session = sessionmaker(bind = engine)
        session = Session()
        yield session
    finally:
        session.close()
