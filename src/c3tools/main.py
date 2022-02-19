import typer

from . import cli

app = typer.Typer()

app.add_typer(cli.random.app, name="random")
