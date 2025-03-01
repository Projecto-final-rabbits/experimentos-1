from pydantic import BaseModel

class ProductSell(BaseModel):
    product_id: int
    units: int
