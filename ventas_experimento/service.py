from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Product
from .schemas import ProductSell

def sell_product_service(product: ProductSell, db: Session):
    db_product = db.query(Product).filter(Product.id == product.product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    if db_product.units < product.units:
        raise HTTPException(status_code=400, detail="Not enough units in stock")
    db_product.units -= product.units
    db.commit()
    db.refresh(db_product)
    return {"product_id": db_product.id, "units": product.units}
