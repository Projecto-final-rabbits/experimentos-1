from dataclasses import dataclass, field
from src.shared.domain.entity import Entity

@dataclass
class Product(Entity):
    name = field()
    quantity = field()
    price = field()
    warehouse_id = field()
    warehouse_name = field()
    warehouse_location = field()
