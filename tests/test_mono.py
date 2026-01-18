"""Tests for the mono CLI tool."""

from __future__ import annotations

from typer.testing import CliRunner

from mono import app

runner = CliRunner()


def test_hello_default() -> None:
    """Test hello command with default argument."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout


def test_hello_with_name() -> None:
    """Test hello command with custom name."""
    result = runner.invoke(app, ["Alice"])
    assert result.exit_code == 0
    assert "Hello, Alice!" in result.stdout


def test_app_help() -> None:
    """Test that help message works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "A minimal Python CLI template" in result.stdout
