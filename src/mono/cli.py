"""CLI commands for mono."""

from __future__ import annotations

import typer

HELP_TEXT = """A minimal Python CLI template.

\b
Examples:
  $ mono
  Hello, World!

  $ mono Alice
  Hello, Alice!

  $ mono "Python Developer"
  Hello, Python Developer!
"""

app = typer.Typer(
    help=HELP_TEXT,
    context_settings={"help_option_names": ["-h", "--help"]},
)


@app.callback(invoke_without_command=True)
def hello(
    name: str = typer.Argument("World", help="Name to greet"),
) -> None:
    """Say hello to someone."""
    typer.echo(f"Hello, {name}!")


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
