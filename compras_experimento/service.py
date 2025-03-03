from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Product
from schemas import ProductCreateDTO
from pubsub import publish_message

def create_product_service(product: ProductCreateDTO, db: Session):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    publish_message("productBought", {"product_id": db_product.id, "units": db_product.units})
    return db_product

def update_product_units_service(product_id: int, units: int, db: Session):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_product.units += units
    db.commit()
    db.refresh(db_product)
    publish_message("productBought", {"product_id": db_product.id, "units": units})
    return db_product
