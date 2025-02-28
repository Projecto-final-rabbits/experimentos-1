from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from compras.domain.models import Base

DATABASE_URL = "sqlite:///./compras.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)