import pydantic

from . import string


class CamelModel(pydantic.BaseModel):
    class Config:
        alias_generator = string.camel
        allow_population_by_field_name = True
        use_enum_values = True
