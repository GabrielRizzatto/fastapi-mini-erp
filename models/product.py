import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Base
from sqlalchemy import  Column, String, Integer, Boolean

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    