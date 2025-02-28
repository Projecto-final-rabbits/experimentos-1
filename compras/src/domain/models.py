from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Compra(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, index=True)
    producto = Column(String, index=True)
    cantidad = Column(Integer)
    precio = Column(Integer)

    def __repr__(self):
        return f"<Compra(id={self.id}, producto='{self.producto}', cantidad={self.cantidad}, precio={self.precio})>"