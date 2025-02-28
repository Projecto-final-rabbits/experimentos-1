from typing import List
from compras.domain.models import Compra
from compras.domain.repositories import CompraRepository

class ComprasService:
    def __init__(self, compra_repository: CompraRepository):
        self.compra_repository = compra_repository

    def create_compra(self, compra: Compra) -> Compra:
        return self.compra_repository.save(compra)

    def get_all_compras(self) -> List[Compra]:
        return self.compra_repository.find_all()

    def get_compra_by_id(self, compra_id: int) -> Compra:
        return self.compra_repository.find_by_id(compra_id)

    def update_compra(self, compra_id: int, compra: Compra) -> Compra:
        existing_compra = self.get_compra_by_id(compra_id)
        if existing_compra:
            existing_compra.update(compra)  # Assuming an update method exists in the Compra model
            return self.compra_repository.save(existing_compra)
        return None

    def delete_compra(self, compra_id: int) -> bool:
        return self.compra_repository.delete(compra_id)