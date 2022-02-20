import sys
import re
import typer

from .. import lib

app = typer.Typer()


@app.command()
def camel():
    input_str = sys.stdin.read()
    typer.echo(lib.string.camel(input_str))


@app.command()
def pascal():
    input_str = sys.stdin.read()
    typer.echo(lib.string.pascal(input_str))
