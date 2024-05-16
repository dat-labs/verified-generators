import os
from typing import Any, Tuple, Iterator
import openai
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from dat_core.pydantic_models.dat_message import DatMessage, Type
from dat_core.connectors.generators.base import GeneratorBase
from verified_generators.openai.specs import OpenAISpecification

class OpenAI(GeneratorBase):
    
    _spec_class = OpenAISpecification
    
    def check_connection(self, config: OpenAISpecification) -> Tuple[bool, Any]:
        try:
            _r = OpenAIEmbeddings(
                openai_api_key=config.connection_specification.openai_api_key,
            ).embed_query('foo')
        except openai.AuthenticationError:
            raise
        return (True, _r)

    def generate(
        self,
        config: OpenAISpecification,
        dat_message: DatMessage
    ) -> Iterator[DatMessage]:
        """
        The generator operation will generator vector chunks

        Args:
            config (OpenAISpecification): The user-provided configuration as specified by
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


if __name__ == '__main__':
    from dat_core.pydantic_models.dat_message import DatDocumentMessage, Data
    s = OpenAI().spec()
    print(s)

    c = OpenAI().check(config=OpenAISpecification.model_validate_json(
        open('generator_config.json').read()),)
    print(c)

    e = OpenAI().generate(
        config=OpenAISpecification.model_validate_json(
            open('generator_config.json').read()),
        dat_message=DatMessage(
            type=Type.RECORD,
            record=DatDocumentMessage(
                data=Data(
                    document_chunk='foo',
                ),
                emitted_at=1,
            ),
        )
    )
    print(list(e))
