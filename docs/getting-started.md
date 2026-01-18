---
icon: lucide/rocket
---

# Getting Started

## Installation

There are several ways to install and use mono:

=== "Try It First (No Install)"

    Use `uvx` to run mono without installing:

    ```bash
    uvx mono Alice
    # Output: Hello, Alice!
    ```

=== "Install as Tool (Recommended)"

    Install mono globally as a tool:

    ```bash
    uv tool install mono
    ```

    Then use it anywhere:

    ```bash
    mono World
    # Output: Hello, World!
    ```

=== "pip/pipx"

    ```bash
    pip install mono
    # or
    pipx install mono
    ```

=== "Use as Template"

    If you want to create your own CLI tool, use mono as a template:

    ```bash
    # Clone the template
    git clone https://github.com/guenp/mono.git my-cli-tool
    cd my-cli-tool
    rm -rf .git && git init
    ```

    See [Customizing](#customizing-the-template) below.

## Verify Installation

```bash
mono --help
```

You should see the help text showing available commands and options.

## Your First Command

The template comes with a simple `hello` command:

```bash
# Default greeting
mono
# Output: Hello, World!

# Greet someone specific
mono Alice
# Output: Hello, Alice!

# Use quotes for multi-word names
mono "Python Developer"
# Output: Hello, Python Developer!
```

## Customizing the Template

If you cloned mono to create your own CLI tool, follow these steps:

### 1. Rename the Package

Replace all occurrences of `mono` with your package name:

```bash
# macOS
find . -type f -not -path './.git/*' -exec sed -i '' 's/mono/mycli/g' {} +

# Linux
find . -type f -not -path './.git/*' -exec sed -i 's/mono/mycli/g' {} +
```

Rename directories:

```bash
mv src/mono src/mycli
mv tests/test_mono.py tests/test_mycli.py
```

### 2. Update Metadata

Edit `pyproject.toml` to update:
- Package `name`
- `description`
- `authors`
- Repository URLs
- Any other metadata

### 3. Set Up Development Environment

```bash
# Install uv if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --group dev --group docs

# Install pre-commit hooks
uv run pre-commit install
```

### 4. Test Your Setup

```bash
# Run tests
uv run pytest

# Try your CLI
uv run python -m mycli
# Output: Hello, World!
```

### 5. Add Your Commands

Edit `src/mycli/cli.py` and replace the example `hello` command with your own:

```python
@app.command()
def process(
    file: Path = typer.Argument(..., help="File to process"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Process a file."""
    if verbose:
        typer.echo(f"Processing {file}")
    # Your implementation here
```

## Next Steps

- Learn about all [commands and options](usage.md)
- Read about the [development workflow](../README.md#development-workflow)
- Check out [customization examples](../README.md#customization-examples)
- Set up [CI/CD and automatic releases](../README.md#building-and-publishing)
