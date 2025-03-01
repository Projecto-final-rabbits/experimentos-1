from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Product
from .schemas import ProductCreate
from .pubsub import publish_message

def create_product_service(product: ProductCreate, db: Session):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    publish_message("product_created", db_product)
    return db_product

def get_product_service(product_id: int, db: Session):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

def update_product_units(product_id: int, units: int, db: Session):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.units += units
    db.commit()
    db.refresh(db_product)
    return db_product

def handle_product_bought(event_data: dict, db: Session):
    product_id = event_data["product_id"]
    units = event_data["units"]
    return update_product_units(product_id, -units, db)

def handle_product_selled(event_data: dict, db: Session):
    product_id = event_data["product_id"]
    units = event_data["units"]
    return update_product_units(product_id, units, db)
