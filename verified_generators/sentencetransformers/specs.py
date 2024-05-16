# generated by datamodel-codegen:
#   filename:  specs.yml
#   timestamp: 2024-05-15T03:48:14+00:00

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Field


class SentenceTransformersSpecification(BaseModel):
    class Config:
        extra = 'allow'

    connection_specification: Dict[str, Any] = Field(
        ...,
        description='ConnectorDefinition specific blob. Must be a valid JSON string.',
    )