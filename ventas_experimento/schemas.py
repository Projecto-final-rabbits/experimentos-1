from pydantic import BaseModel

class ProductSell(BaseModel):
    id: int
    units: int
