from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime
from .rules import IdInmutableRule
from .exceptions import IsShouldBeInmutable

@dataclase
class Entity:
    id: UUID = field()
    created_at: datetime = field()
    updated_at: datetime = field()

    @classmethod
    def get_random_id(self) -> UUID:
        return uuid4()

    @id.setter
    def id(self, id: UUID) -> None:
        if not IdInmutableRule(self).es_valido():
            raise IsShouldBeInmutable()
        self._id = self.siguiente_id()