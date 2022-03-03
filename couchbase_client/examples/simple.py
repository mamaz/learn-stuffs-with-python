from typing import Dict
from uuid import uuid4
from couchbase.collection import CBCollection
from couchbase.cluster import Bucket, Cluster, ClusterOptions, QueryOptions
from couchbase_core.cluster import PasswordAuthenticator
from couchbase.n1ql import QueryResult, QueryMetaData
import json
import time

print('connecting...')

cluster = Cluster('couchbase://13.212.13.21', ClusterOptions(
    PasswordAuthenticator('Administrator', 'aku dirimu dirinya')
))

example_bucket: Bucket = cluster.bucket('example')
cb_coll: CBollection = example_bucket.default_collection()

def insert_doc(some_doc: Dict):
    doc_id = some_doc.get('id', str(uuid4()))
    cb_coll.upsert(doc_id, some_doc)

def get_doc(doc_id: str) -> str:
    return cb_coll.get(doc_id).content_as[dict]

def query_doc(doc_id: str) -> QueryResult:
    return cluster.query("SELECT * FROM `example` WHERE id = $doc_id", bucket='example', doc_id=doc_id)


if __name__ == "__main__":
    print('fetching...')

    end = 0.0
    start = 0.0
    try:
        start = time.perf_counter()
        res = query_doc('123')

        for r in res:
            print(r)

        end = time.perf_counter()
    except Exception as e:
        print(f"error: {e}")
    finally:
        elapsed = (end - start) * 1000
        print(f'elapsed: {elapsed} ms')