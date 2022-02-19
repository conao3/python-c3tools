import typer

from ..lib import random

app = typer.Typer()


@app.command()
def uuid():
    typer.echo(random.uuid4())
