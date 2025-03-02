from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv
load_dotenv()

from database import SessionLocal, engine, Base, get_db
from schemas import ProductSell
from service import sell_product_service
from pubsub import publish_message
from enums import EventType
from pubsub import subscribe_to_product_created, subscribe_to_product_updated
from service import handle_product_created, handle_product_updated


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/sell_product/")
def sell_product(product: ProductSell, db: Session = Depends(get_db)):
    sold_product = sell_product_service(product, db)
    return sold_product

@app.on_event("startup")
def startup_event():
    def callback(message):
        event_data = message.data.decode("utf-8")
        event_type = message.attributes.get("event_type")
        db = SessionLocal()

        print("*** message received", event_data, event_type)
        if event_type == EventType.product_created.value:
            handle_product_created(event_data, db)
            message.ack()
        elif event_type == EventType.product_updated.value:
            handle_product_updated(event_data, db)        
            message.ack()
        

    subscribe_to_product_created(callback)
    subscribe_to_product_updated(callback) 
