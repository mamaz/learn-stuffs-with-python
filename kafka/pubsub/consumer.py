from typing import Dict
from confluent_kafka import DeserializingConsumer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer
from confluent_kafka.serialization import StringDeserializer
from confluent_kafka.error import KafkaException
from pubsub.schema import schema_str

def subscribe(topic: str, consumer_conf: Dict):
    consumer = DeserializingConsumer(consumer_conf)
    consumer.subscribe([topic])

    print(f'start listening on topic: {topic}, config: {consumer_conf}')
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            if msg.error():
                raise KafkaException(msg.error())

            user = msg.value()
            if user is not None:
                print(f"received user: {user}")

        except Exception as e:
            print(f"Exception at listening for incoming: {e}")
            break

    consumer.close()

if __name__ == "__main__":
    topic = "test_subscriber"

    sr_conf = {"url": "http://localhost:8081"}
    schema_registry_client = SchemaRegistryClient(sr_conf)
    avro_deserializer = AvroDeserializer(
        schema_str,
        schema_registry_client,
        from_dict=None
    )
    consumer_conf = {
        "bootstrap.servers": "localhost:9092",
        "key.deserializer": StringDeserializer('utf-8'),
        "value.deserializer": avro_deserializer,
        "group.id": "test_subscriber_group",
        "auto.offset.reset": "earliest"
    }

    subscribe(topic, consumer_conf)
