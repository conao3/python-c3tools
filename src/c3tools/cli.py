import typer

app = typer.Typer()

@app.command()
def create():
    print("create")
