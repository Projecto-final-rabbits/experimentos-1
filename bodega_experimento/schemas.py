from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    units: int

class ProductCreateDTO(ProductBase):
    ...

class ProductUpdateDTO(ProductBase):
    id: int

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
