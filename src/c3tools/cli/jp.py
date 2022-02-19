import sys
import json
import jmespath
import typer

app = typer.Typer()


@app.command()
def jp(query: str = typer.Option("@", help="JMESPath query")):
    input = sys.stdin.read()
    typer.echo(json.dumps(jmespath.search(query, json.loads(input)), indent=2))
