import sys
import re
from typing import Any
import typer
import json
from .. import lib

app = typer.Typer()


@app.command()
def oas():
    endpoint = input("Endpoint[/get_sound_info_by_gras_getData]: ")

    params = []
    while True:
        try:
            input_str = input('Param[<json>]: ')
        except EOFError:
            break
        if input_str == "":
            break

        param = json.loads(input_str)
        params.append(param)

    response = input("Response: ")

    typer.echo(f"{endpoint=}, {params=}, {response=}")


@app.command()
def oas_response():
    tgt = json.loads(sys.stdin.read())
    typer.echo(json.dumps(lib.openapi.gen_schema(tgt), indent=2, ensure_ascii=False))


@app.command()
def oas_parse_parameter():
    params = []
    regexp = re.compile(r"([^ ]*): (?:(.*) )?// (.*)")
    while True:
        try:
            input_str = input()
        except EOFError:
            break
        if input_str == "":
            break

        if m := re.match(regexp, input_str):
            name, example, description = m.groups()
            if m := re.match(r"(.*) +[^ ]+必須", description):
                description = m.groups()[0]
                required = True
            else:
                required = False

            params.append({
                "name": name,
                "example": example,
                "description": description,
                "required": bool(required)
            })

        else:
            typer.echo(f"parse error: {input_str}")
            typer.echo(f"  expected: {regexp.pattern}")

    for param in params:
        typer.echo(json.dumps(param, ensure_ascii=False))
