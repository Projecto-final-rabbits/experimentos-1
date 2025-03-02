from google.cloud import pubsub_v1
from google.oauth2 import service_account
import os
import threading
import json

from enums import EventType


credentials = service_account.Credentials.from_service_account_file("cloud-key.json")
publisher = pubsub_v1.PublisherClient(credentials=credentials)
subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

project_id = os.getenv("CLOUD_PROJECT_ID")
topic_id = os.getenv("PRODUCT_TOPIC")
created_product_sub = os.getenv("PRODUCT_CREATED_SUB")
updated_product_sub = os.getenv("PRODUCT_UPDATED_SUB")


def publish_message(data: dict):
    topic_path = publisher.topic_path(project_id, topic_id)
    data_str = json.dumps({
        "id": data["id"],
        "name": data["name"],
        "units": data["units"]
    })
    future = publisher.publish(topic_path, data_str.encode("utf-8"), event_type=EventType.product_selled.value)
    future.result()

def subscribe_to_product_created(callback):
    subscription_path = subscriber.subscription_path(project_id, created_product_sub)
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    threading.Thread(target=streaming_pull_future.result).start()

def subscribe_to_product_updated(callback):
    subscription_path = subscriber.subscription_path(project_id, updated_product_sub)
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    threading.Thread(target=streaming_pull_future.result).start()
