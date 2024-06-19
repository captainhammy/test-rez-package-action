"""Dummy package.py file for build testing."""

name = "test_package"
version = "0.0.1"

build_system = "cmake"

tests = {
    "unit": {"command": "python -m pytest tests/", "requires": ["pytest"]},
    "specific": {"command": "python -m pytest tests/", "requires": ["pytest"]},
}


def commands():
    """Run commands."""
    pass
