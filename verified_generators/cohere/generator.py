import os
from typing import Any, Optional, Tuple, Iterator
import cohere
from dat_core.pydantic_models.dat_message import DatMessage
from dat_core.connectors.generators.base import GeneratorBase
from verified_generators.cohere.specs import CohereSpecification


class Cohere(GeneratorBase):
    _spec_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'specs.yml')

    def __init__(self) -> None:
        super().__init__()

    def check_connection(self, config: CohereSpecification) -> Tuple[bool, Optional[Any]]:
        cohere_client = get_cohere_client(
            config.connection_specification.cohere_api_key
        )
        try:
            _r = cohere_client.embed(
                texts=['foo'],
                input_type='search_query',
                embedding_types=['float'],
            )
        except cohere.core.api_error.ApiError:
            raise
        return True, _r

    def generate(
        self,
        config: CohereSpecification,
        dat_message: DatMessage
    ) -> Iterator[DatMessage]:
        """
        The generator operation will generator vector chunks

        Args:
            config (CohereSpecification): The user-provided configuration as specified by
              the generator's spec.
            document_chunks: DatMessage containing 
        Yields:
            Iterator[Dict]: Each row should be wrapped around a DatMessage obj
        """
        cohere_client = get_cohere_client(
            config.connection_specification.cohere_api_key
        )
        input_type = "search_query"
        dat_message.record.data.vectors = cohere_client.embed(
            texts=[dat_message.record.data.document_chunk],
            model=config.connection_specification.cohere_model,
            input_type=input_type,
            embedding_types=['float'],
        )
        yield dat_message

def get_cohere_client(cohere_api_key):
    return cohere.Client(api_key=cohere_api_key)