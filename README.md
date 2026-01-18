# mono - Python CLI Template

[![PyPI](https://img.shields.io/pypi/v/mono)](https://pypi.org/project/mono/)
[![Python](https://img.shields.io/pypi/pyversions/mono)](https://pypi.org/project/mono/)
[![License](https://img.shields.io/github/license/guenp/mono)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/guenp/mono/pytest.yml?label=tests)](https://github.com/guenp/mono/actions/workflows/pytest.yml)

<img src="logo.svg" align="right" width="100" />

A minimal, production-ready template for Python CLI tools. Get started building your CLI in minutes with modern tooling, comprehensive testing, and CI/CD out of the box.

## Features

This template provides:

- **Modern Python packaging** with [hatchling](https://hatch.pypa.io/) and [hatch-vcs](https://github.com/ofek/hatch-vcs) for automatic versioning
- **CLI framework** using [Typer](https://typer.tiangolo.com/) with type hints and autocomplete support
- **Code quality** with [Ruff](https://docs.astral.sh/ruff/) for linting/formatting and [mypy](https://mypy-lang.org/) for type checking
- **Testing** with [pytest](https://pytest.org/) and coverage reporting
- **Pre-commit hooks** configured and ready to use
- **CI/CD** with GitHub Actions (testing on multiple platforms/Python versions)
- **Documentation** infrastructure with [Zensical](https://github.com/zensical/zensical)
- **Automatic releases** to PyPI when you tag versions

## Using This Template

### 1. Create Your Repository

Click "Use this template" on GitHub or:

```bash
git clone https://github.com/guenp/mono.git my-cli-tool
cd my-cli-tool
rm -rf .git && git init
```

### 2. Customize the Package

Replace all occurrences of `mono` with your package name:

```bash
# macOS
find . -type f -not -path './.git/*' -exec sed -i '' 's/mono/yourpackage/g' {} +

# Linux
find . -type f -not -path './.git/*' -exec sed -i 's/mono/yourpackage/g' {} +
```

Rename the package directory:

```bash
mv src/mono src/yourpackage
mv tests/test_mono.py tests/test_yourpackage.py
```

Update `pyproject.toml`:
- Change `name`, `description`, and `authors`
- Update repository URLs
- Adjust dependencies as needed

### 3. Install Development Environment

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv sync --group dev --group docs

# Install pre-commit hooks
uv run pre-commit install
```

### 4. Start Building

Replace the example `hello` command in `src/yourpackage/cli.py` with your own commands:

```python
@app.command()
def yourcommand(
    arg: str = typer.Argument(..., help="Description"),
    flag: bool = typer.Option(False, "--flag", help="Enable feature"),
) -> None:
    """Your command description."""
    # Your implementation here
    typer.echo(f"Running with {arg}")
```

## Quick Start (Using This Template As-Is)

Install the example CLI:

```bash
uv tool install mono
# or: uvx mono World
```

Try it out:

```bash
mono
# Output: Hello, World!

mono Alice
# Output: Hello, Alice!

mono --help
# See available options
```

## Development Workflow

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=yourpackage

# Run specific test
uv run pytest tests/test_yourpackage.py::test_hello_default
```

### Code Quality

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Type check
uv run mypy src tests

# Run all pre-commit hooks
uv run pre-commit run --all-files
```

### Building and Publishing

The template includes automatic PyPI publishing via GitHub Actions when you push a tag:

```bash
# Create a new version tag
git tag v0.1.0
git push origin v0.1.0
```

Or build locally:

```bash
# Build wheel and sdist
uv build

# Install your local build
uv pip install dist/yourpackage-*.whl
```

### Documentation

Documentation is built with Zensical:

```bash
# Build docs
uv run zensical build

# Serve docs locally
uv run zensical serve
```

Update the docs in the `docs/` directory and customize `zensical.toml`.

## Project Structure

```
.
├── .github/
│   └── workflows/        # CI/CD workflows (tests, release, docs)
├── docs/                 # Documentation source files
│   ├── index.md
│   ├── getting-started.md
│   └── usage.md
├── src/
│   └── yourpackage/
│       ├── __init__.py   # Package initialization
│       ├── cli.py        # CLI commands (Typer app)
│       └── _version.py   # Auto-generated version file
├── tests/
│   ├── conftest.py       # Pytest configuration
│   └── test_yourpackage.py
├── pyproject.toml        # Package metadata and tool configuration
├── zensical.toml         # Documentation configuration
└── CLAUDE.md             # Development notes for AI assistants
```

## What's Included

### Dependencies

**Core:**
- `typer>=0.15` - CLI framework with rich features

**Development:**
- `pytest>=8` - Testing framework
- `pytest-cov>=4` - Coverage reporting
- `mypy>=1.14` - Static type checker
- `ruff>=0.9` - Fast linter and formatter
- `pre-commit>=4` - Git hook framework

**Documentation:**
- `zensical` - Documentation builder
- `markdown-gfm-admonition` - Enhanced markdown support

### CI/CD Workflows

1. **pytest.yml** - Runs tests on Python 3.12+ across Linux, macOS, and Windows
2. **release.yml** - Publishes to PyPI when you tag a version
3. **docs.yml** - Builds and deploys documentation to GitHub Pages

### Configuration Files

- **pyproject.toml** - All tool configuration in one place
- **zensical.toml** - Documentation site settings
- **.pre-commit-config.yaml** - Pre-commit hook configuration
- **CLAUDE.md** - Project context for AI coding assistants

## Customization Examples

### Adding a New Command

```python
# src/yourpackage/cli.py

@app.command()
def process(
    input_file: Path = typer.Argument(..., help="Input file to process"),
    output: Path | None = typer.Option(None, "--output", "-o"),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
) -> None:
    """Process a file and optionally save results."""
    if verbose:
        typer.echo(f"Processing {input_file}")

    # Your logic here
    result = do_processing(input_file)

    if output:
        output.write_text(result)
        typer.echo(f"Saved to {output}")
    else:
        typer.echo(result)
```

### Adding Dependencies

```bash
# Add a runtime dependency
uv add requests

# Add a dev dependency
uv add --group dev ipython

# Update lockfile
uv lock
```

### Adding Tests

```python
# tests/test_yourpackage.py

def test_process_command() -> None:
    """Test the process command."""
    result = runner.invoke(app, ["process", "input.txt"])
    assert result.exit_code == 0
    assert "Processing" in result.stdout
```

## Why This Template?

This template embodies Python packaging best practices as of 2025:

- **`pyproject.toml`** - Single source of truth for all configuration
- **`src/` layout** - Prevents accidental imports of uninstalled code
- **Type hints** - Full type coverage with mypy
- **Modern tools** - Ruff (fast) instead of multiple slower tools
- **Comprehensive CI** - Test across platforms and Python versions
- **Automatic versioning** - Git tags become package versions
- **Developer experience** - Pre-commit hooks catch issues before CI

## Contributing

Contributions are welcome! This template is designed to be:

- **Minimal** - Only essential features, easy to understand
- **Modern** - Uses current best practices and tools
- **Practical** - Everything works out of the box

Please open an issue or PR if you have suggestions.

## License

MIT - feel free to use this template for any project.

## Acknowledgments

Built with modern Python tooling:
- [Typer](https://typer.tiangolo.com/) for the CLI framework
- [Hatch](https://hatch.pypa.io/) for packaging
- [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [uv](https://github.com/astral-sh/uv) for fast dependency management

This template is inspired by https://github.com/basnijholt/trueloc.
