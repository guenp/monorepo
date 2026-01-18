"""Core greeting functionality."""

from __future__ import annotations


def say_hello(name: str = "World") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"
