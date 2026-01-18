"""Tests for mono.one subpackage."""

from __future__ import annotations

from mono.one import say_hi


def test_say_hi_default() -> None:
    """Test say_hi with default argument."""
    result = say_hi()
    assert result == "Hi, Friend!"


def test_say_hi_with_name() -> None:
    """Test say_hi with custom name."""
    result = say_hi("Bob")
    assert result == "Hi, Bob!"


def test_import_from_one() -> None:
    """Test that say_hi can be imported from mono.one."""
    from mono.one import say_hi as imported_func

    assert callable(imported_func)
    assert imported_func("Test") == "Hi, Test!"
