import io
import json
from typing import Dict
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from avro import schema


def process_user(user: Dict):
    SCHEMA = schema.parse("""
    {
        "namespace": "com.kata.user",
        "type": "record",
        "name": "User",
        "fields": [
            {"name": "name", "type": "string"},
            {"name": "favorite_number", "type": ["int", "null"]},
            {"name": "favorite_color", "type": ["string", "null"]}
        ]
    }
    """)

    buffer = io.BytesIO()
    writer = DataFileWriter(buffer, DatumWriter(), SCHEMA)
    writer.append(user)
    writer.append(user) # we can append more than one user
    writer.flush()

    buffer.seek(0)
    data_written = buffer.read();
    print(f'Avro binary writen to buffer: {data_written}')
    writer.close()

    read_buf = io.BytesIO(data_written)
    reader = DataFileReader(read_buf, DatumReader())
    for user in reader:
        print(f'USER: {user}')
    reader.close()

if __name__ == "__main__":
    process_user({'name': 'Eli', 'favorite_number': 42, 'favorite_color': 'black'})
