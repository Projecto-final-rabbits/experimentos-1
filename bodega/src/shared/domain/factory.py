from abc import ABC, abstractmethod
from .repository import DomainMapper
from .mixins import ValidarReglasMixin

class Factory(ABC, ValidarReglasMixin):
    @abstractmethod
    def create_object(self, obj: any, mapeador: DomainMapper=None) -> any:
        ...