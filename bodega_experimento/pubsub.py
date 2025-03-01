from google.cloud import pubsub_v1
from google.oauth2 import service_account
import os
import threading

credentials = service_account.Credentials.from_service_account_file("cloud-key.json")
publisher = pubsub_v1.PublisherClient(credentials=credentials)
subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

print("***", os.getenv("CLOUD_PROJECT_ID"))

project_id = os.getenv("CLOUD_PROJECT_ID")
topic_id = os.getenv("PRODUCT_TOPIC")
subscription_id = os.getenv("PRODUCT_SELLED_SUB")

def publish_message(event_type: str, data: dict):
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, data.encode("utf-8"), event_type=event_type)
    future.result()

def subscribe_to_topic(callback):
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    threading.Thread(target=streaming_pull_future.result).start()
