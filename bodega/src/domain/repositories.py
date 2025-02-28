from typing import Protocol, List
from .models import Bodega

class BodegaRepository(Protocol):
    def get_bodega(self, bodega_id: int) -> Bodega:
        ...

    def list_bodegas(self) -> List[Bodega]:
        ...

    def add_bodega(self, bodega: Bodega) -> None:
        ...

    def update_bodega(self, bodega: Bodega) -> None:
        ...

    def delete_bodega(self, bodega_id: int) -> None:
        ...