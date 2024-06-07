import os
from typing import Any, Optional, Tuple
import cohere
from dat_core.connectors.generators.base import GeneratorBase
from dat_core.pydantic_models import ConnectorSpecification
from verified_generators.cohere.specs import CohereSpecification


class Cohere(GeneratorBase):
    _spec_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specs.yml')
    
    co = cohere.Client(api_key="YOUR_API_KEY")
    def check_connection(self, config: ConnectorSpecification) -> Tuple[bool, Optional[Any]]:
        # Implement your connection check logic here
        return False, {}

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

        dat_message.record.data.vectors = OpenAIEmbeddings(
            openai_api_key=config.connection_specification.openai_api_key,
            model=config.connection_specification.openai_model,
        ).embed_query(dat_message.record.data.document_chunk)
        yield dat_message
