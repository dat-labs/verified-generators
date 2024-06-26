import os
from typing import Any, Tuple, Iterator
from sentence_transformers import SentenceTransformer
from dat_core.pydantic_models.dat_message import DatMessage, Type
from dat_core.connectors.generators.base import GeneratorBase
from verified_generators.sentencetransformers.specs import SentenceTransformersSpecification


class SentenceTransformers(GeneratorBase):

    _spec_class = SentenceTransformersSpecification

    def check_connection(self, config: SentenceTransformersSpecification) -> Tuple[bool, Any]:
        return (True, None)

    def generate(
        self,
        config: SentenceTransformersSpecification,
        dat_message: DatMessage
    ) -> Iterator[DatMessage]:
        """
        The generator operation will generator vector chunks

        Args:
            config (SentenceTransformersSpecification): The user-provided configuration as specified by
              the generator's spec.
            document_chunks: DatMessage containing 
        Yields:
            Iterator[Dict]: Each row should be wrapped around a DatMessage obj
        """

        dat_message.record.data.vectors = [_ for _ in SentenceTransformer('all-MiniLM-L6-v2').encode(
            dat_message.record.data.document_chunk)]
        # list comprehension to convert Numpy array to Python list
        yield dat_message

if __name__ == '__main__':
    from dat_core.pydantic_models.dat_message import DatDocumentMessage, Data
    e = SentenceTransformers().generate(
        config=SentenceTransformersSpecification.model_validate_json(
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