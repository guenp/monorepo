"""Tests for mono_two subpackage."""

from __future__ import annotations

from mono_two import say_bye


def test_say_bye_default() -> None:
    """Test say_bye with default argument."""
    result = say_bye()
    assert result == "Goodbye, Friend!"


def test_say_bye_with_name() -> None:
    """Test say_bye with custom name."""
    result = say_bye("Charlie")
    assert result == "Goodbye, Charlie!"


def test_import_from_two() -> None:
    """Test that say_bye can be imported from mono_two."""
    from mono_two import say_bye as imported_func

    assert callable(imported_func)
    assert imported_func("Test") == "Goodbye, Test!"
