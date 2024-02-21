import json
from os import getenv
from pytest import fixture

@fixture
def valid_generator_config_json():
    """Will yield a the JSON str of a valid generator config

    Yields:
        str: JSON str of a valid generator config
    """
    yield json.dumps({
        "name": "OpenAI", 
        "connectionSpecification": {
            "openai_api_key": getenv('OPENAI_API_KEY')
            }
        })