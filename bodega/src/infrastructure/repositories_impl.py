from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .dtos import WarehouseEntity
from src.domain.repositories import DomainRepository

DATABASE_URL = "sqlite:///./bodega.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class WarehouseRepositoryImpl(DomainRepository):
    def __init__(self):
        self.db = SessionLocal()

    def add(self, warehouse: WarehouseEntity):
        self.db.add(warehouse)
        self.db.commit()
        self.db.refresh(warehouse)
        return warehouse

    def get_by_id(self, warehouse_id: int):
        return self.db.query(WarehouseEntity).filter(WarehouseEntity.id == warehouse_id).first()

    def get_all(self):
        return self.db.query(WarehouseEntity).all()

    def update(self, warehouse: WarehouseEntity):
        self.db.merge(warehouse)
        self.db.commit()
        return warehouse

    def delete(self, warehouse_id: int):
        bodega = self.get(warehouse_id)
        if bodega:
            self.db.delete(bodega)
            self.db.commit()
        return bodega