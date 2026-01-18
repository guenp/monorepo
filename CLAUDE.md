# mono - Development Notes

See [README.md](README.md) for user-facing documentation.

## Overview

`mono` is a minimal Python CLI template designed to help developers quickly bootstrap production-ready CLI tools. This document contains development notes for AI coding assistants and contributors.

## Project Structure

```
src/mono/
├── __init__.py  # Package initialization with version and app exports
└── cli.py       # Typer CLI application with commands
```

## Key Design Principles

1. **Minimal** - Only include essential features. Users can add what they need.
2. **Modern** - Use current Python best practices (2025):
   - `pyproject.toml` for all configuration
   - `src/` layout to prevent import issues
   - Type hints everywhere
   - Ruff for fast linting/formatting
3. **Production-Ready** - CI/CD, testing, docs infrastructure all configured
4. **Template-First** - Easy to customize and rename for new projects

## Implementation Details

### Versioning

Version is automatically determined from git tags using `hatch-vcs`:
- The `_version.py` file is auto-generated during build
- In development, falls back to "0.0.0" if `_version.py` doesn't exist
- Tag format: `v1.2.3`

### CLI Structure

The CLI uses Typer with a simple structure:
- Main app defined in `cli.py`
- Individual commands decorated with `@app.command()`
- Type hints used for argument/option parsing
- Help text from docstrings and parameter help

### Testing

Tests use pytest with Typer's test utilities:
- `CliRunner` for invoking commands
- Simple assertions on exit codes and output
- No complex fixtures needed for the template

### Package Layout

Uses `src/` layout benefits:
- Prevents importing uninstalled package
- Clean separation of source and tests
- Better for editable installs

## Development Workflow

### Adding Features to the Template

When adding features:
1. Keep it minimal - only add if truly essential
2. Document clearly in README
3. Update tests
4. Ensure it works across platforms (CI tests this)

### Making Template Changes

When modifying the template itself:
1. Test that the template works for new users
2. Ensure customization steps in README are accurate
3. Test the rename/customization process manually

## Configuration

### pyproject.toml

Single source of truth for:
- Package metadata
- Dependencies (runtime and development groups)
- Tool configuration (ruff, mypy, pytest, coverage)
- Build system (hatchling + hatch-vcs)

### CI/CD

Three workflows:
1. **pytest.yml** - Run tests on every push/PR
2. **release.yml** - Publish to PyPI on git tags
3. **docs.yml** - Build docs and deploy to GitHub Pages

## Common Tasks

### Updating Dependencies

```bash
uv add package-name  # Add runtime dependency
uv add --group dev package-name  # Add dev dependency
uv lock  # Update lockfile
```

### Testing Changes

```bash
uv run pytest  # Run tests
uv run mypy src tests  # Type check
uv run ruff check .  # Lint
uv run ruff format .  # Format
```

### Building

```bash
uv build  # Create wheel and sdist
```

## Template Customization (For Users)

Users should:
1. Clone/fork the repository
2. Find-and-replace `mono` with their package name
3. Rename directories and files
4. Update metadata in `pyproject.toml`
5. Replace the `hello` command with their own

See README.md for detailed instructions.

## Future Considerations

Potential additions (but keep minimal):
- [ ] Optional async command support
- [ ] Example of command groups/subcommands
- [ ] Rich console output examples
- [ ] Configuration file handling example

Don't add unless clearly beneficial for most CLI tools.
