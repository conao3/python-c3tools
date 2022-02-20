import json
import sys

import jmespath
import typer
import yaml

from .. import lib

app = typer.Typer()


@app.command(name="json")
def json_cli(query: str = typer.Option("@", help="JMESPath query")):
    input = sys.stdin.read()
    typer.echo(json.dumps(jmespath.search(query, json.loads(input)), indent=2))


@app.command(name="yaml")
def yaml_cli(
    query: str = typer.Option("@", help="JMESPath query"),
    indent_list: bool = typer.Option(False, "--indent-list", "-i", help="Indent lists"),
):
    input = sys.stdin.read()
    dct = jmespath.search(query, json.loads(input))

    if indent_list:
        typer.echo(yaml.dump(dct, Dumper=lib.yaml.ListIndentDumper, sort_keys=False, indent=2, allow_unicode=True))
    else:
        typer.echo(yaml.dump(dct, sort_keys=False, indent=2))
