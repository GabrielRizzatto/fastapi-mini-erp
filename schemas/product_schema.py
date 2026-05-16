from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: Decimal = Field(..., max_digits=10, decimal_places=2, gt=0)
    current_stock: int = Field(default=0, ge=0)
    min_stock: int = Field(default=0, ge=0)

    class Config:
        from_attributes = True