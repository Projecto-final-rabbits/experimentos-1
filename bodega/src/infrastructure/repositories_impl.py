from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bodega.domain.models import BodegaModel
from bodega.domain.repositories import BodegaRepository

DATABASE_URL = "sqlite:///./bodega.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BodegaRepositoryImpl(BodegaRepository):
    def __init__(self):
        self.db = SessionLocal()

    def create(self, bodega: BodegaModel):
        self.db.add(bodega)
        self.db.commit()
        self.db.refresh(bodega)
        return bodega

    def get(self, bodega_id: int):
        return self.db.query(BodegaModel).filter(BodegaModel.id == bodega_id).first()

    def list(self):
        return self.db.query(BodegaModel).all()

    def update(self, bodega: BodegaModel):
        self.db.merge(bodega)
        self.db.commit()
        return bodega

    def delete(self, bodega_id: int):
        bodega = self.get(bodega_id)
        if bodega:
            self.db.delete(bodega)
            self.db.commit()
        return bodega