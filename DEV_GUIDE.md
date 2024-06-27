# Development guide

## Introduction

This is a detailed guide to help you develop your own connector for `verified-generators` and ensure that all your tests pass.

### Generate stub files for your verified-generator actor
```bash
dat-cli init
```

Follow the onscreen instructions and you will be met with these lines in your terminal output.

```text
...
dat-dev/verified-generators/verified_generators/{your-generator-connector}/specs.yml written.
dat-dev/verified-generators/verified_generators/{your-generator-connector}/specs.py written.
dat-dev/verified-generators/verified_generators/{your-generator-connector}/generator.py written.
dat-dev/verified-generators/verified_generators/{your-generator-connector}/tests/conftest.py written.
dat-dev/verified-generators/verified_generators/{your-generator-connector}/tests/test_{your-generator-connector}.py written.
```

Your `verified-generators` directory should look something like this:
```text
verified_generators/
├── {your-generator-connector}/
│   ├── generator.py
│   ├── specs.py
│   ├── specs.yml
│   └── tests/
│       ├── conftest.py
│       └── test_{your-generator-connector}.py
└── verified_generator_0/
    ├── ...
    └── ...
```

We have a detailed description for what each file does under our [docs](http://path/to/docs). Here we are providing a short description of them.

### `specs.yml`

Here, we can add any additional parameters (as keys) that we want our generator to have under `connection_specification`.

E.g. If you are developing a Cohere generator actor, you might want to ask for the `cohere_api_key` and `cohere_model` as part of `connection_specification`. You can add it like so:
Example:
```yml
description: Specification of an actor (source/embeddingsgenerator/destination)
type: object
...
file truncated for brevity
...
  connection_specification:
    description: ConnectorDefinition specific blob. Must be a valid JSON string.
    type: object
    additionalProperties: true
    properties:
      cohere_api_key:
        type: string
        description: "Cohere API key"
        title: "Cohere API key"
        order: 0
      cohere_model:
        type: string
        default: "embed-english-v3.0"
        description: "Cohere model"
        title: "Cohere model"
        order: 1
```

### `specs.py`

This file contains the `specs.yml` file as a [Pydantic](https://docs.pydantic.dev/latest/concepts/models/) model. You can generate it using [`datamodel-codegen`](https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/) or edit manually like so:
Example:
```python
'''
file truncated for brevity
'''
class ConnectionSpecification(BaseModel):
    class Config:
        extra = 'allow'

    cohere_api_key: str = Field(..., description='Cohere key', title='Cohere API key')
    cohere_model: Optional[str] = Field(
        'embed-english-v3.0', description='Cohere model', title='Cohere model'
    )
'''
file truncated for brevity
'''
```

### `generator.py`

There are two methods in the file that need to be implemented. Stub code has already been generated.

#### `check_connection(...):`
```python
# TODO
```

#### `generate(...):`
```python
# TODO
```

## Running tests
```bash
pytest verified_generators/{your-generator-connector}/tests/test_{your-generator-connector}.py 
```
