---
icon: lucide/terminal
---

# Usage

## Basic Usage

The mono template comes with a simple greeting command to demonstrate CLI functionality.

### Default Behavior

Running `mono` without arguments uses the default greeting:

```bash
mono
# Output: Hello, World!
```

### Custom Greeting

Pass a name as an argument to customize the greeting:

```bash
mono Alice
# Output: Hello, Alice!
```

### Multi-Word Names

Use quotes for names with spaces:

```bash
mono "Python Developer"
# Output: Hello, Python Developer!
```

## Help and Documentation

### Get Help

```bash
mono --help
# or
mono -h
```

Shows all available commands, arguments, and options.

## Building Your Own Commands

The template is designed to be extended with your own commands. Here are examples of common CLI patterns:

### Simple Command

Add a basic command with required arguments:

```python
# src/mono/cli.py

@app.command()
def greet(
    name: str = typer.Argument(..., help="Person to greet"),
    greeting: str = typer.Option("Hello", help="Greeting to use"),
) -> None:
    """Greet someone with a custom greeting."""
    typer.echo(f"{greeting}, {name}!")
```

Usage:
```bash
mono greet Alice
# Output: Hello, Alice!

mono greet Bob --greeting "Hi"
# Output: Hi, Bob!
```

### File Processing Command

Process input files with optional output:

```python
from pathlib import Path

@app.command()
def process(
    input_file: Path = typer.Argument(..., help="Input file to process"),
    output: Path | None = typer.Option(None, "--output", "-o", help="Output file"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose output"),
) -> None:
    """Process a file and optionally save results."""
    if verbose:
        typer.echo(f"Processing {input_file}...")

    # Read and process
    content = input_file.read_text()
    result = content.upper()  # Example: convert to uppercase

    if output:
        output.write_text(result)
        typer.echo(f"Saved to {output}")
    else:
        typer.echo(result)
```

Usage:
```bash
mono process input.txt
mono process input.txt -o output.txt
mono process input.txt -o output.txt --verbose
```

### Interactive Prompts

Get user input interactively:

```python
@app.command()
def configure() -> None:
    """Configure the application interactively."""
    name = typer.prompt("What's your name?")
    age = typer.prompt("What's your age?", type=int)
    confirm = typer.confirm("Are these details correct?")

    if confirm:
        typer.echo(f"Configured for {name}, age {age}")
    else:
        typer.echo("Configuration cancelled")
```

Usage:
```bash
mono configure
# What's your name?: Alice
# What's your age?: 30
# Are these details correct? [y/N]: y
# Configured for Alice, age 30
```

### Multiple Commands (Subcommands)

Create command groups for organizing related functionality:

```python
# src/mono/cli.py

# Main app
app = typer.Typer(help="Your CLI tool")

# Create a subcommand group
db_app = typer.Typer(help="Database commands")
app.add_typer(db_app, name="db")

@db_app.command()
def init() -> None:
    """Initialize the database."""
    typer.echo("Database initialized")

@db_app.command()
def migrate() -> None:
    """Run database migrations."""
    typer.echo("Running migrations...")
```

Usage:
```bash
mono db init
# Output: Database initialized

mono db migrate
# Output: Running migrations...

mono db --help
# Shows all database-related commands
```

### Progress Bars

Show progress for long-running operations:

```python
import time

@app.command()
def download(url: str) -> None:
    """Download a file with progress."""
    items = range(100)

    with typer.progressbar(items, label="Downloading") as progress:
        for item in progress:
            time.sleep(0.01)  # Simulate work

    typer.echo("Download complete!")
```

### Rich Output

Use Typer's built-in styling for colorful output:

```python
@app.command()
def status() -> None:
    """Show system status with colors."""
    typer.secho("✓ Service running", fg=typer.colors.GREEN, bold=True)
    typer.secho("⚠ Warning: High CPU usage", fg=typer.colors.YELLOW)
    typer.secho("✗ Error: Disk full", fg=typer.colors.RED, bold=True)
```

### Configuration Files

Read configuration from a file:

```python
import json
from pathlib import Path

@app.command()
def run(
    config: Path = typer.Option(
        Path("config.json"),
        "--config",
        "-c",
        help="Configuration file",
    ),
) -> None:
    """Run with configuration from file."""
    if not config.exists():
        typer.secho(f"Config file not found: {config}", fg=typer.colors.RED)
        raise typer.Exit(1)

    settings = json.loads(config.read_text())
    typer.echo(f"Running with config: {settings}")
```

## Error Handling

Exit gracefully with appropriate status codes:

```python
@app.command()
def validate(file: Path) -> None:
    """Validate a file."""
    if not file.exists():
        typer.secho(f"Error: {file} not found", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    if not file.suffix == ".json":
        typer.secho("Error: File must be JSON", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    typer.secho("✓ File is valid", fg=typer.colors.GREEN)
```

## Testing Your Commands

The template includes pytest configuration for testing CLI commands:

```python
# tests/test_mono.py
from typer.testing import CliRunner
from mono.cli import app

runner = CliRunner()

def test_custom_command() -> None:
    """Test a custom command."""
    result = runner.invoke(app, ["greet", "Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.stdout

def test_with_options() -> None:
    """Test command with options."""
    result = runner.invoke(app, ["greet", "Bob", "--greeting", "Hi"])
    assert result.exit_code == 0
    assert "Hi, Bob!" in result.stdout

def test_error_handling() -> None:
    """Test error conditions."""
    result = runner.invoke(app, ["validate", "missing.json"])
    assert result.exit_code == 1
    assert "not found" in result.stdout
```

Run tests with:

```bash
uv run pytest
uv run pytest --cov=mono  # With coverage
```

## Advanced Patterns

### Environment Variables

Read configuration from environment variables:

```python
import os

@app.command()
def connect() -> None:
    """Connect using environment variables."""
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "5432"))

    typer.echo(f"Connecting to {host}:{port}")
```

### Custom Callbacks

Run code before/after commands:

```python
@app.callback()
def callback(
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Global options that apply to all commands."""
    if verbose:
        typer.echo("Verbose mode enabled")
```

### Shell Completion

Typer supports shell completion out of the box:

```bash
# Install completion for your shell
mono --install-completion

# Or manually:
# Bash
mono --show-completion bash >> ~/.bashrc

# Zsh
mono --show-completion zsh >> ~/.zshrc

# Fish
mono --show-completion fish >> ~/.config/fish/completions/mono.fish
```

## Best Practices

1. **Use type hints** - Typer relies on type hints for validation and help text
2. **Add help text** - Document all commands, arguments, and options
3. **Validate inputs** - Check file existence, validate ranges, etc.
4. **Use appropriate exit codes** - 0 for success, non-zero for errors
5. **Provide feedback** - Use progress bars, status messages, and colors
6. **Write tests** - Test all commands and edge cases
7. **Keep commands focused** - Each command should do one thing well

## Next Steps

- Read the [Typer documentation](https://typer.tiangolo.com/) for more features
- Check out [rich](https://rich.readthedocs.io/) for even fancier terminal output
- Explore the [Click documentation](https://click.palletsprojects.com/) (Typer is built on Click)
