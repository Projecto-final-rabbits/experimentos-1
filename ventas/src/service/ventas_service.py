from typing import List
from ventas.domain.models import Venta
from ventas.domain.repositories import VentaRepository

class VentasService:
    def __init__(self, repository: VentaRepository):
        self.repository = repository

    def create_venta(self, venta: Venta) -> Venta:
        return self.repository.save(venta)

    def get_venta(self, venta_id: int) -> Venta:
        return self.repository.find_by_id(venta_id)

    def list_ventas(self) -> List[Venta]:
        return self.repository.find_all()

    def update_venta(self, venta_id: int, venta: Venta) -> Venta:
        existing_venta = self.repository.find_by_id(venta_id)
        if existing_venta:
            existing_venta.update(venta)  # Assuming an update method exists in the Venta model
            return self.repository.save(existing_venta)
        return None

    def delete_venta(self, venta_id: int) -> bool:
        return self.repository.delete(venta_id)