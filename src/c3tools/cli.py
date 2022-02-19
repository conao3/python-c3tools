import typer

import c3tools.random

app = typer.Typer()

app.add_typer(c3tools.random.app, name="random")
