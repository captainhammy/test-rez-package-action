"""Dummy package.py file for build testing."""

name = "test_package"
version = "0.0.1"

build_system = "cmake"

# Pass -c to pytest, so it doesn't try and load the pyproject.toml from the parent folder
tests = {
    "unit": {"command": "python -m pytest tests/", "requires": ["pytest"]},
    "specific": {"command": "python -m pytest -c tests/", "requires": ["pytest"]},
}


def commands():
    """Run commands."""
    pass
