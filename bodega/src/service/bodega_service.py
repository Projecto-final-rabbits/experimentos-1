from typing import List
from bodega.domain.models import Bodega
from bodega.domain.repositories import BodegaRepository

class BodegaService:
    def __init__(self, repository: BodegaRepository):
        self.repository = repository

    def create_bodega(self, bodega: Bodega) -> Bodega:
        return self.repository.add(bodega)

    def get_bodega(self, bodega_id: int) -> Bodega:
        return self.repository.get(bodega_id)

    def list_bodegas(self) -> List[Bodega]:
        return self.repository.list_all()

    def update_bodega(self, bodega_id: int, bodega: Bodega) -> Bodega:
        return self.repository.update(bodega_id, bodega)

    def delete_bodega(self, bodega_id: int) -> None:
        self.repository.delete(bodega_id)