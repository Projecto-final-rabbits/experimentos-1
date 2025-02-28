from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from .entity import Entity

class BusinessRule(ABC):

    __message: str ='bussiness rule error'

    def __init__(self, message):
        self.__message = message

    def error_message(self) -> str:
        return self.__message

    @abstractmethod
    def is_valid(self) -> bool:
        ...

    def __str__(self):
        return f"{self.__class__.__name__} - {self.__message}"
    
class IdInmutableRule(BusinessRule):

    _entity: Entity

    def __init__(self, entity: Entity, message="Id should be inmutable"):
        super().__init__(message)
        self._entity = entity

    def is_valid(self) -> bool:
        hasId = self._entity and self._entity.id
        return not hasId
        