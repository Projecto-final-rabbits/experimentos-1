from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()

project_id = "your-gcp-project-id"
topic_id = "your-topic-id"

def publish_message(event_type: str, data: dict):
    topic_path = publisher.topic_path(project_id, topic_id)
    future = publisher.publish(topic_path, data.encode("utf-8"), event_type=event_type)
    future.result()
