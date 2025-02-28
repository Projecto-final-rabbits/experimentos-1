from typing import Protocol, List
from .models import Venta

class IVentaRepository(Protocol):
    def create(self, venta: Venta) -> Venta:
        ...

    def get_by_id(self, venta_id: int) -> Venta:
        ...

    def list(self) -> List[Venta]:
        ...

    def update(self, venta: Venta) -> Venta:
        ...

    def delete(self, venta_id: int) -> None:
        ...