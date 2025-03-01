from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

from database import SessionLocal, engine, Base, get_db
from schemas import ProductCreate, ProductResponse
from service import create_product_service, get_product_service, handle_product_bought, handle_product_selled
from pubsub import subscribe_to_topic  


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product_service(product, db)

@app.get("/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return get_product_service(product_id, db)

@app.on_event("startup")
def startup_event():
    def callback(message):
        event_data = message.data.decode("utf-8")
        event_type = message.attributes.get("event_type")
        db = SessionLocal()

        if event_type == "productBought":
            handle_product_bought(event_data, db)
        elif event_type == "productSelled":
            handle_product_selled(event_data, db)
        
        message.ack()

    subscribe_to_topic(callback)  
