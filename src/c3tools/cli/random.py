import string
import typer

from ..lib import random

app = typer.Typer()


@app.command()
def uuid():
    typer.echo(random.uuid4())


@app.command()
def chars(
    length: int = typer.Option(..., help="Length of the string"),
    prefix: str = typer.Option(""),
    suffix: str = typer.Option(""),
):
    typer.echo(prefix + random.chars(length, population=string.digits + "abcdef") + suffix)
