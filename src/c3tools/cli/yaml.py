import json
import sys

import jmespath
import typer
import yaml

app = typer.Typer()


@app.command(name="json")
def json_cli(query: str = typer.Option("@", help="JMESPath query")):
    input = sys.stdin.read()
    typer.echo(json.dumps(jmespath.search(query, yaml.safe_load(input)), indent=2))


@app.command(name="yaml")
def yaml_cli(query: str = typer.Option("@", help="JMESPath query")):
    input = sys.stdin.read()
    typer.echo(yaml.dump(jmespath.search(query, yaml.safe_load(input)), sort_keys=False, indent=2))
