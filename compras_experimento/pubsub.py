from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

project_id = "your-gcp-project-id"
topic_id = "your-topic-id"
subscription_id = "your-subscription-id"

def publish_message(event_type: str, data: dict):
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, data.encode("utf-8"), event_type=event_type)
    future.result()

def subscribe_to_topic(callback):
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    streaming_pull_future.result()
