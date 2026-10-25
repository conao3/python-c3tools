import pydantic

from . import string


class CamelModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        alias_generator=string.camel,
        validate_by_name=True,
        use_enum_values=True,
    )
