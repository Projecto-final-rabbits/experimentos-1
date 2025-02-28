from abc import ABC, abstractmethod
from .dtos import DTO

class ApplicationMapper(ABC):
    @abstractmethod
    def extern_to_dto(self, externo: any) -> DTO:
        ...

    @abstractmethod
    def dto_to_extern(self, dto: DTO) -> any:
        ...