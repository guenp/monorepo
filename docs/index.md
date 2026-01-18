---
icon: lucide/rocket
---

# mono

**A minimal Python CLI template**

A production-ready template for building Python CLI tools with modern tooling, comprehensive testing, and CI/CD out of the box.

## Quick Start

Install the example CLI:

```bash
uv tool install mono
# or run directly: uvx mono World
```

Try it out:

```bash
mono hello
# Output: Hello, World!

mono hi Alice
# Output: Hi, Alice!

mono bye Bob
# Output: Goodbye, Bob!
```

> [!NOTE]
> This example demonstrates the optional monorepo structure with three subpackages (`mono-core`, `mono-one`, `mono-two`). You can keep this structure or simplify to a single package.

[Get Started →](getting-started.md){ .md-button .md-button--primary }
[View Usage →](usage.md){ .md-button }

## Features

This template provides:

- ✨ **Modern Python packaging** with hatchling and hatch-vcs for automatic versioning
- 🎯 **CLI framework** using Typer with type hints and autocomplete support
- ✅ **Code quality** with Ruff for linting/formatting and mypy for type checking
- 🧪 **Testing** with pytest and coverage reporting
- 🪝 **Pre-commit hooks** configured and ready to use
- 🚀 **CI/CD** with GitHub Actions (testing on multiple platforms/Python versions)
- 📚 **Documentation** infrastructure with Zensical
- 📦 **Automatic releases** to PyPI when you tag versions

## Why This Template?

This template embodies Python packaging best practices as of 2025:

- **`pyproject.toml`** - Single source of truth for all configuration
- **`src/` layout** - Prevents accidental imports of uninstalled code
- **Type hints** - Full type coverage with mypy
- **Modern tools** - Ruff (fast) instead of multiple slower tools
- **Comprehensive CI** - Test across platforms and Python versions
- **Automatic versioning** - Git tags become package versions
- **Developer experience** - Pre-commit hooks catch issues before CI

## Using This Template

### 1. Create Your Repository

Click "Use this template" on GitHub or clone:

```bash
git clone https://github.com/guenp/mono.git my-cli-tool
cd my-cli-tool
```

### 2. Customize the Package

**Choose your structure:**

=== "Simple Package (Recommended)"

    Remove the example subpackages:
    ```bash
    rm -rf mono-core mono-one mono-two
    ```

    Update `pyproject.toml` to remove subpackage dependencies:
    ```toml
    dependencies = [
        "typer>=0.15",
        # Remove: mono-core, mono-one, mono-two
    ]
    # Remove the [tool.uv.sources] section
    ```

=== "Monorepo Structure"

    Keep the subpackages and customize them for your needs. Useful when you need to publish multiple packages separately.

**Then, for either option:**

Replace `mono` with your package name:

```bash
# macOS
find . -type f -not -path './.git/*' -exec sed -i '' 's/mono/yourpackage/g' {} +

# Linux
find . -type f -not -path './.git/*' -exec sed -i 's/mono/yourpackage/g' {} +
```

Rename directories:

```bash
mv src/mono src/yourpackage
# If keeping subpackages:
# mv mono-core yourpackage-core
# mv mono-one yourpackage-one
```

### 3. Start Building

Replace the example `hello` command in `src/yourpackage/cli.py` with your own commands.

See the [Getting Started Guide](getting-started.md) for detailed instructions.

## What's Included

### Dependencies

**Core:**
- `typer>=0.15` - CLI framework with rich features

**Development:**
- `pytest>=8`, `pytest-cov>=4` - Testing and coverage
- `mypy>=1.14` - Static type checker
- `ruff>=0.9` - Fast linter and formatter
- `pre-commit>=4` - Git hook framework

**Documentation:**
- `zensical` - Documentation builder
- `markdown-gfm-admonition` - Enhanced markdown

### CI/CD Workflows

1. **pytest.yml** - Runs tests on Python 3.12+ across Linux, macOS, and Windows
2. **release.yml** - Publishes to PyPI when you tag a version
3. **docs.yml** - Builds and deploys documentation to GitHub Pages

## Project Structure

This template supports two project structures:

=== "Simple Package (Default)"

    ```
    .
    ├── .github/workflows/    # CI/CD workflows
    ├── docs/                 # Documentation source
    ├── src/yourpackage/      # Your package code
    │   ├── __init__.py
    │   └── cli.py
    ├── tests/                # Test files
    ├── pyproject.toml        # Package metadata
    └── zensical.toml         # Docs configuration
    ```

=== "Monorepo (Optional)"

    ```
    .
    ├── .github/workflows/
    ├── docs/
    ├── yourpackage-core/          # Separate subpackage
    │   ├── pyproject.toml
    │   ├── README.md
    │   └── src/yourpackage_core/
    ├── yourpackage-one/           # Another subpackage
    │   ├── pyproject.toml
    │   ├── README.md
    │   └── src/yourpackage_one/
    ├── src/yourpackage/           # Main CLI package
    │   ├── __init__.py
    │   └── cli.py
    ├── tests/
    ├── pyproject.toml             # Main project config
    └── zensical.toml
    ```

**When to use the monorepo structure:**

- You need to publish multiple packages separately to PyPI
- Different parts have different dependencies
- You want independent versioning for subpackages
- You're building a plugin ecosystem or modular toolkit

## License

MIT - feel free to use this template for any project.

## Built With

- [Typer](https://typer.tiangolo.com/) - CLI framework
- [Hatch](https://hatch.pypa.io/) - Packaging
- [Ruff](https://docs.astral.sh/ruff/) - Linting and formatting
- [uv](https://github.com/astral-sh/uv) - Fast dependency management
