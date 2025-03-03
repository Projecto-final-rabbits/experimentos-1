from sqlalchemy.orm import Session
from fastapi import HTTPException
import json

from models import Product
from schemas import ProductCreateDTO, ProductResponse, ProductUpdateDTO
from pubsub import publish_message
from enums import EventType

def create_product_service(product: ProductCreateDTO, db: Session):    
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    _pusblish_event(EventType.product_created, db_product.__dict__)
    return db_product

def update_product_units_service(product_id: int, units: int, db: Session):
    db_product: Product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.units = units
    db.commit()
    db.refresh(db_product)
    _pusblish_event(EventType.product_updated, db_product.__dict__)
    return db_product

def get_product_service(product_id: int, db: Session) -> ProductResponse:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


def handle_product_selled(event_data: dict, db: Session):
    try:
        product = json.loads(event_data)
    except json.JSONDecodeError:
        print("Error: No se pudo deserializar el evento")
        return
    
    product_id = product["id"]
    units = product["units"]
    
    update_product_units_service(product_id, units, db)

def _pusblish_event(event: EventType, db_product: Product):
    publish_message(event, db_product)
    return db_product
