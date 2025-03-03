from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()

from database import SessionLocal, engine, Base, get_db
from schemas import ProductCreateDTO, ProductResponse
from service import create_product_service, update_product_units_service


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreateDTO, db: Session = Depends(get_db)):
    db_product = create_product_service(product, db)
    return db_product

@app.post("/products/{product_id}/update_units", response_model=ProductResponse)
def update_product_units(product_id: int, units: int, db: Session = Depends(get_db)):
    db_product = update_product_units_service(product_id, units, db)
    return db_product
