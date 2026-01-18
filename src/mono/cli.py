"""CLI commands for mono."""

from __future__ import annotations

import typer

from mono.core import say_hello
from mono.one import say_hi
from mono.two import say_bye

HELP_TEXT = """A minimal Python CLI monorepo template.

\b
Examples:
  $ mono hello World
  Hello, World!

  $ mono hi Alice
  Hi, Alice!

  $ mono bye Bob
  Goodbye, Bob!
"""

app = typer.Typer(
    help=HELP_TEXT,
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.command()
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone (using mono.core)."""
    message = say_hello(name)
    typer.echo(message)


@app.command()
def hi(
    name: str = typer.Argument("Friend", help="Name to greet"),
) -> None:
    """Say hi to someone (using mono.one)."""
    message = say_hi(name)
    typer.echo(message)


@app.command()
def bye(
    name: str = typer.Argument("Friend", help="Name to say goodbye to"),
) -> None:
    """Say goodbye to someone (using mono.two)."""
    message = say_bye(name)
    typer.echo(message)


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
