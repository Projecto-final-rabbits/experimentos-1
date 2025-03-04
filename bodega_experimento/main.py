from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from faker import Faker
import random

load_dotenv()

from database import SessionLocal, engine, Base, get_db
from schemas import ProductCreateDTO, ProductUpdateDTO, ProductResponse
from service import create_product_service, get_product_service, handle_product_selled, update_product_units_service, get_all_products_service, delete_all_products_service
from pubsub import subscribe_to_topic  
from enums import EventType


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/product/", response_model=ProductResponse)
def create_product(product: ProductCreateDTO, db: Session = Depends(get_db)):
    return create_product_service(product, db)

@app.patch("/product/add/units", response_model=ProductResponse)
def update_product_units(product_updated_dto: ProductUpdateDTO, db: Session = Depends(get_db)):
    product_id = product_updated_dto.id
    units = product_updated_dto.units
    return update_product_units_service(product_id, units, db)

@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_service(product_id, db)

@app.on_event("startup")
def startup_event():
    def callback(message):
        event_data = message.data.decode("utf-8")
        event_type = message.attributes.get("event_type")
        db = SessionLocal()

        if event_type == EventType.product_selled.value:
            handle_product_selled(event_data, db)
        
        message.ack()
        

    subscribe_to_topic(callback)  

fake = Faker()
@app.post("/populate_db/")
def populate_db(quantity: int = Query(10, description="Cantidad de productos a crear"), db: Session = Depends(get_db)):
    created_products = []

    for _ in range(quantity):
        product_data = ProductCreateDTO(
            id=random.randint(100, 9999),
            name=fake.word(),
            description=fake.sentence(),
            units=random.randint(300, 1000))
        created_product = create_product_service(product_data, db)
        created_products.append(created_product)

    return {"message": f"{quantity} productos creados exitosamente", "products": created_products}

@app.get("/products/", response_model=list[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    return get_all_products_service(db)

@app.delete("/products/")
def delete_all_products(db: Session = Depends(get_db)):
    delete_all_products_service(db)
    return {"message": "Todos los productos han sido eliminados"}