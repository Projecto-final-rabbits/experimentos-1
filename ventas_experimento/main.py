from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from .database import SessionLocal, engine, Base
from .schemas import ProductSell
from .service import sell_product_service
from .pubsub import publish_message

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/sell_product/")
def sell_product(product: ProductSell, db: Session = SessionLocal()):
    sold_product = sell_product_service(product, db)
    publish_message("productSelled", sold_product)
    return sold_product
