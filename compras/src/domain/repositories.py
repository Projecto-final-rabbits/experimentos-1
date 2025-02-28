from abc import ABC, abstractmethod
from typing import List
from .models import Compra

class CompraRepository(ABC):
    @abstractmethod
    def create(self, compra: Compra) -> Compra:
        pass

    @abstractmethod
    def get_by_id(self, compra_id: int) -> Compra:
        pass

    @abstractmethod
    def list(self) -> List[Compra]:
        pass

    @abstractmethod
    def update(self, compra: Compra) -> Compra:
        pass

    @abstractmethod
    def delete(self, compra_id: int) -> None:
        pass