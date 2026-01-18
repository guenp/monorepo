"""A minimal Python CLI template."""

from __future__ import annotations

from mono.cli import app

try:
    from mono._version import __version__, __version_tuple__
except ImportError:
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)

__all__ = [
    "__version__",
    "__version_tuple__",
    "app",
]

if __name__ == "__main__":
    app()
