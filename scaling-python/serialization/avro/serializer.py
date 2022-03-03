"""
Avro serializer and deserielizer wrapper
"""
import io
from typing import Dict, cast, Union
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from avro import schema

def serialize(data: Dict, dict_schema: str, codec:str = 'null') -> bytes:
    """
    Serialize data from Dict to Avro formatted binary

    Args:
        dict (Any): Dictionary

    Returns:
        bytes: Avro bytes representing serialized Dict
    """
    assert type(data).__name__ == 'dict', 'data should be Dict'
    assert dict_schema is not None

    avro_schema = schema.parse(dict_schema)
    io_buf = io.BytesIO()

    # write to buffer
    writer = DataFileWriter(io_buf, DatumWriter(), avro_schema, codec=codec)
    writer.append(data)
    writer.flush()

    io_buf.seek(0)
    data_bytes = io_buf.read()
    writer.close()

    return data_bytes

def deserialiaze(avro_bytes: bytes) -> Union[Dict, None]:
    """
    Deserialize data from avro bytes to Dict,
    raise TypeError if avro_bytes is not avro formatted bytes

    Args:
        avro_bytes (bytes): Dict data in avro bytes

    Returns:
        Dict: data or None
    """
    assert avro_bytes is not None

    read_buf = io.BytesIO(avro_bytes)
    reader = DataFileReader(read_buf, DatumReader())
    for data in reader:
        reader.close()
        assert isinstance(data, dict), 'avro bytes is not dictionary, but {type(data).__name__}'
        return cast(Dict, data)

    return None
