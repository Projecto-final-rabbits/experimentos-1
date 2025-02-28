from dataclasses import dataclass

@dataclass(frozen=True)
class ProductDTO:
    name: str
    quantity: int
    price: float
    warehouse_id: int
    warehouse_name: str
    warehouse_location: str