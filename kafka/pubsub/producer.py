from uuid import uuid4
from typing import Dict
from confluent_kafka.serialization import SerializationContext, StringSerializer
from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from .schema import schema_str

class User:
    def __init__(self, name: str, favorite_number: int, favorite_color: str):
        self.name = name
        self.favorite_number = favorite_number
        self.favorite_color = favorite_color


def user_to_dict(user: User, ctx: SerializationContext):
    return {
        "name": user.name,
        "favorite_number": user.favorite_number,
        "favorite_color": user.favorite_color,
    }

def publish(topic: str, data: object, producer_conf: Dict):
    print(f'produce {data} to topic {topic} config {producer_conf}')
    producer = SerializingProducer(producer_conf)

    def on_delivered(err, msg):
        if err is not None:
            print(f"delivery failed on message keyc {msg.key()}")
            return

        print(f"message delivered key: {msg.key} topic: {msg.topic} partition: {msg.partition} offset: {msg.offset}")

    try:
        producer.produce(
            topic=topic,
            key=str(uuid4()),
            value=data,
            # on_delivery=on_delivered
        )
    except Exception as e:
        print(f'Error happens when producing {e}')

    producer.poll(1.0)

if __name__ == "__main__":
    schema_registry_conf = {'url': 'http://localhost:8081'}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    avro_serializer = AvroSerializer(
        schema_str,
        schema_registry_client,
        user_to_dict
    )

    producer_conf = {'bootstrap.servers': 'localhost:9092',
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': avro_serializer}
    publish(
        "test_subscriber",
        User("mamaz", favorite_number=13, favorite_color='black'),
        producer_conf
    )
