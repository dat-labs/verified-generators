import os
from pytest import fixture

@fixture()
def valid_connection_object():
    yield {
        "cohere_api_key": os.getenv('COHERE_API_KEY'),
    }

@fixture()
def valid_dat_record_message():
    yield {
        "type": "RECORD",
        "log":None,
        "spec":None,
        "connectionStatus":None,
        "catalog":None,
        "record": {
            "data": {
                "document_chunk": "foo"
            }
        }
    }