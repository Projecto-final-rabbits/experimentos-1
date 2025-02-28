
from dataclasses import dataclass

from src.shared.domain.factory import Factory
from src.shared.domain.repository import DomainMapper

from .models import Product, Warehouse, Supplier
from .exceptions import DoesntExistObjectTypeOnDomain

@dataclass
class _WarehouseFactory(Factory):
    def create_object(self, obj, mapper: DomainMapper = None):
        if isinstance(obj, Warehouse):
            return mapper.entity_to_dto(obj)
        
        warehouse = mapper.dto_to_entity(obj)
        # validate rules
        return warehouse

@dataclass
class _ProductFactory(Factory):
    def create_object(self, obj, mapper: DomainMapper = None):
        if isinstance(obj, Product):
            return mapper.entity_to_dto(obj)
        
        product = mapper.dto_to_entity(obj)
        # validate rules
        return product

@dataclass
class _SupplierFactory(Factory):
    def create_object(self, obj, mapper: DomainMapper = None):
        if isinstance(obj, Supplier):
            return mapper.entity_to_dto(obj)
        
        supplier = mapper.dto_to_entity(obj)
        # validate rules
        return supplier
        

class WarehouseFactory(Factory):
    def create_object(self, obj, mapper: DomainMapper = None):
        if mapper.get_type() == Warehouse.__class__:
            return _WarehouseFactory().create_object(obj, mapper)
        elif mapper.get_type() == Product.__class__:
            return _ProductFactory().create_object(obj, mapper)
        elif mapper.get_type() == Supplier.__class__:
            return _SupplierFactory().create_object(obj, mapper)
        raise DoesntExistObjectTypeOnDomain()
    