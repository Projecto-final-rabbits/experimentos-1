from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    units: int

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
