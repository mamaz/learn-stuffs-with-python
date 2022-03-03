"""Example of Avro serialization from reading schema from a file
to serialize and write it to another file, then reading it, then displaying to stdout

Avro lacks documentation of using
"""

from avro.schema import parse
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

with open("user.avsc", "rb") as file:
    data = file.read()
    schema = parse(data)
    print(f'{schema}')

    with open("user.avro", "wb") as filewriter:
        writer = DataFileWriter(filewriter, datum_writer=DatumWriter(), writers_schema=schema)
        writer.append({
            "name":"Alyssa",
            "favorite_number": 13,
            "favorite_color": "red",
        })
        writer.append({
            "name":"Mamazo",
            "favorite_number": 10,
            "favorite_color": "cyan",
        })
        writer.close() # should be closed

        reader = DataFileReader(open("user.avro", "rb"), DatumReader())
        for user in reader:
            print(user)
            print(type(user))
        reader.close() #should also be closed

