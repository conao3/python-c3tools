import sys
import re
from typing import Any, Optional
import typer
import json
import yaml

from . import clitypes
from .. import lib

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
                    "tags": [],
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
                    "parameters": [elm.dict() for elm in inpt.params],
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
    typer.echo(json.dumps(lib.openapi.gen_parameter_schema(params), indent=2, ensure_ascii=False,))


@app.command()
def oas_response():
    tgt = json.loads(sys.stdin.read())
    typer.echo(json.dumps(lib.openapi.gen_schema(tgt), indent=2, ensure_ascii=False))


@app.command()
def oas_parse_parameter():
    for param in [clitypes.OasParameterType.parse(elm) for elm in lib.stdin.readlines()]:
        typer.echo(json.dumps(param, ensure_ascii=False))
