"""Dummy test file that outputs data to indicate it ran."""

# Standard Library
import os
import pathlib


def test_set_output():
    """Write to output data."""
    output_path = pathlib.Path(os.environ["GITHUB_OUTPUT"])

    with output_path.open("a", encoding="utf-8") as fp:
        fp.write("package_test_ran=1\n")
