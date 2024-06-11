from verified_generators.cohere.generator import Cohere
from verified_generators.cohere.specs import CohereSpecification
from dat_core.pydantic_models import DatConnectionStatus, DatMessage
from conftest import *


def test_check(valid_connection_object):
    check_connection_tpl = Cohere().check(
        config=CohereSpecification(
            name='Cohere',
            connection_specification=valid_connection_object,
            module_name='cohere'
        )
    )
    assert isinstance(check_connection_tpl, DatConnectionStatus)
    assert check_connection_tpl.status.name == 'SUCCEEDED'


def test_generate(valid_connection_object, valid_dat_record_message):
    config = CohereSpecification(
        name='Cohere',
        connection_specification=valid_connection_object,
        module_name='cohere'
    )

    cohere = Cohere()
    records = cohere.generate(
        config=config,
        dat_message=DatMessage(**valid_dat_record_message),
    )
    for record in records:
        assert DatMessage.model_validate(record)
