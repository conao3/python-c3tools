import json
import sys

import typer
import yaml

from .. import lib
from . import clitypes

app = typer.Typer()


@app.command()
def oas():
    inpt = clitypes.OasInputType.parse_obj(yaml.safe_load(sys.stdin.read()))
    endpoint_pascal = lib.string.pascal(inpt.endpoint_main)

    res = {
        "paths": {
            inpt.endpoint: {
                "get": {
                    "summary": "",
                    "tags": inpt.tags,
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/{endpoint_pascal}",
                                    },
                                    "examples": {
                                        "example-1": {
                                            "value": inpt.response,
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "parameters": [
                        elm.dict()
                        if isinstance(elm, clitypes.OasParameterType)
                        else {
                            "$ref": f"#/components/parameters/{elm.ref}",
                        }
                        if isinstance(elm, clitypes.OasRefParameterType)
                        else (_ for _ in ()).throw(ValueError(f"Invalid type: {elm.__class__.__name__}"))
                        for elm in inpt.params
                    ],
                },
            },
        },
        "components": {
            "schemas": {
                endpoint_pascal: lib.openapi.gen_schema(inpt.response),
            },
        },
    }

    typer.echo(json.dumps(res, indent=2))


@app.command()
def oas_parameter():
    params = [json.loads(elm) for elm in lib.stdin.readlines() if elm]
    typer.echo(
        json.dumps(
            lib.openapi.gen_parameter_schema(params),
            indent=2,
            ensure_ascii=False,
        )
    )


@app.command()
def oas_response():
    arg = json.loads(sys.stdin.read())
    typer.echo(json.dumps(lib.openapi.gen_schema(arg), indent=2, ensure_ascii=False))


@app.command()
def oas_parse_parameter():
    for param in [clitypes.OasParameterType.parse(elm) for elm in lib.stdin.readlines()]:
        typer.echo(json.dumps(param, ensure_ascii=False))
