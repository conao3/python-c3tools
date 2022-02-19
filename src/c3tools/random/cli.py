import typer

from . import uuid as uuid_

app = typer.Typer()


@app.command()
def uuid():
    print(uuid_.gen())
