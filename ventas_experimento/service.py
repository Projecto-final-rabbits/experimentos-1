from sqlalchemy.orm import Session
from fastapi import HTTPException
import json

from models import Product
from schemas import ProductSell
from pubsub import publish_message
from enums import EventType

def sell_product_service(product: ProductSell, db: Session):
    db_product = db.query(Product).filter(Product.id == product.id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if db_product.units < product.units:
        raise HTTPException(status_code=400, detail="Not enough units in stock")
    db_product.units -= product.units
    db.commit()
    db.refresh(db_product)

    _pusblish_event(EventType.product_selled, db_product.__dict__)

    return db_product.__dict__

def _update_product_units_service(product_id: int, units: int, db: Session):
    db_product: Product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.units = units
    db.commit()
    db.refresh(db_product)
    return db_product

def _create_product_service(product: dict, db: Session):
    db_product = Product(**product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def handle_product_updated(event_data: str, db: Session):
    try:
        product_data = json.loads(event_data)
    except json.JSONDecodeError:
        print("Error: No se pudo deserializar el evento en Ventas")
        return
    product_id = int(product_data["id"])
    units = int(product_data["units"])
    _update_product_units_service(product_id, units, db)

def handle_product_created(event_data: dict, db: Session):
    new_product = json.loads(event_data)
    _create_product_service(new_product, db)

def get_product_service(product_id: int, db: Session):
    return db.query(Product).filter(Product.id == product_id).first()

def _pusblish_event(event: EventType, db_product: Product):
    publish_message(event,db_product)
    return db_product
