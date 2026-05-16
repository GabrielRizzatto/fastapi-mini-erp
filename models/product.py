import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import Base
from sqlalchemy import  Column, String, Integer, Boolean, Numeric

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    current_stock = Column(Integer, nullable=False, default=0)
    min_stock = Column(Integer, nullable=False, default=0)
    is_active = Column(Boolean, default=True)