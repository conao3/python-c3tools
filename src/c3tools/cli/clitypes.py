import re
from typing import Any, Optional

import pydantic

from .. import lib


class OasParameterType(lib.pydantic.CamelModel):
    name: str
    example: Optional[str]
    description: str
    required: bool

    @classmethod
    def parse(cls, arg: str) -> "OasParameterType":
        regexp = re.compile(r"([^ ]*): (?:(.*) )?// (.*)")

        if m := re.match(regexp, arg):
            name, example, description = m.groups()
            if m := re.match(r"(.*) +[^ ]+必須", description):
                description = m.groups()[0]
                required = True
            else:
                required = False

            return cls(
                name=name,
                example=example,
                description=description,
                required=required,
            )
        else:
            raise Exception(f"Invalid parameter: {arg}, expected: {regexp.pattern}")


class OasInputType(lib.pydantic.CamelModel):
    summary: str = pydantic.Field(...)
    tags: list[str] = pydantic.Field(...)
    endpoint: str = pydantic.Field(...)
    endpoint_main: str = pydantic.Field(...)
    params: list[OasParameterType] = pydantic.Field(...)
    response: dict[str, Any] = pydantic.Field(...)

    @pydantic.validator("params", pre=True)
    def validate_params(cls, v) -> list[OasParameterType]:
        if isinstance(v, str):
            return [OasParameterType.parse(elm) for elm in lib.subr.keep(v.split("\n"))]

        if isinstance(v, list):
            if errval := lib.subr.keep_if(lambda elm: not isinstance(elm, OasParameterType), v):
                raise ValueError(
                    f"""\
Invalid type:
    expected: list[OasParameterType]
    got: {[str(type(elm)) for elm in errval]}
    got[raw]: {list(errval)} {len(errval)}
"""
                )

            return v

        raise ValueError(f"Invalid type: expected: list[OasParameterType] or str, got: {type(v)}, raw: {v}")

    @pydantic.root_validator(pre=True)
    def root_validator(cls, values) -> dict[str, Any]:
        if "endpoint_main" in values:
            return values

        endpoint_regexp = re.compile(r"/?(.*)(?:_getData)?")
        if m := re.match(endpoint_regexp, values["Endpoint"]):
            values["endpoint_main"] = m.groups()[0]
        else:
            raise Exception(f"Invalid endpoint: {values['Endpoint']}, expected: {endpoint_regexp.pattern}")

        return values
