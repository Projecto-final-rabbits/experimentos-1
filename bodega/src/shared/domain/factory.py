from abc import ABC, abstractmethod
from .repository import DomainMapper
from .mixins import ValidarReglasMixin
from typing import TypeVar

T = TypeVar('T')

class Factory(ABC, ValidarReglasMixin):
    @abstractmethod
    def create_object(self, obj: T, mapeador: DomainMapper=None) -> T:
        ...