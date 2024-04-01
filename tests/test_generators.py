import yaml
from dat_core.pydantic_models.connector_specification import ConnectorSpecification
from dat_core.pydantic_models.dat_connection_status import Status
from dat_core.pydantic_models.dat_message import DatMessage, Type, DatDocumentMessage, Data
from dat_core.pydantic_models.stream_metadata import StreamMetadata
from verified_generators.openai.generator import OpenAI
from conftest import *


def test_generators_spec():
    """
    GIVEN None
    WHEN spec() is called on a valid Generator class
    THEN spec stated in ./specs/ConnectorSpecification.yml is returned
    """

    spec = OpenAI().spec()
    with open('verified_generators/openai/specs/openai-specs.yml') as yaml_in:
        schema = yaml.safe_load(yaml_in)
        assert schema == spec


def test_generators_check(valid_generator_config_json):
    """
    GIVEN a valid connection_specification JSON config
    WHEN check() is called on a valid Generator class
    THEN no error is raised
    """
    check = OpenAI().check(
        config=ConnectorSpecification.model_validate_json(
            valid_generator_config_json))
    assert check.status == Status.SUCCEEDED


def test_generators_generate(valid_generator_config_json):
    """
    GIVEN a valid connection_specification JSON config
    WHEN generate() is called on a valid Generator class
    THEN a generator is returned with metadata intact and vectors populated
    """
    metadata = StreamMetadata(dat_source='bar', dat_stream='paz')
    generate = OpenAI().generate(
        config=ConnectorSpecification.model_validate_json(
            valid_generator_config_json),
        dat_message=DatMessage(
            type=Type.RECORD,
            record=DatDocumentMessage(
                data=Data(
                    document_chunk='foo',
                    metadata=metadata,
                ),
                emitted_at=1,
            ),
        )
    )
    for dm in generate:
        assert dm.record.data.metadata == metadata
        assert len(dm.record.data.vectors)
