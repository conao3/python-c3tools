import typer

from . import cli

app = typer.Typer()

app.add_typer(cli.random.app, name="random")
app.add_typer(cli.json.app, name="json")
app.add_typer(cli.yaml.app, name="yaml")
app.add_typer(cli.glams.app, name="glams")
app.add_typer(cli.string.app, name="string")
