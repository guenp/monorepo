"""Tests for mono.core subpackage."""

from __future__ import annotations

from mono.core import say_hello


def test_say_hello_default() -> None:
    """Test say_hello with default argument."""
    result = say_hello()
    assert result == "Hello, World!"


def test_say_hello_with_name() -> None:
    """Test say_hello with custom name."""
    result = say_hello("Alice")
    assert result == "Hello, Alice!"


def test_import_from_core() -> None:
    """Test that say_hello can be imported from mono.core."""
    from mono.core import say_hello as imported_func

    assert callable(imported_func)
    assert imported_func("Test") == "Hello, Test!"
