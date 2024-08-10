"""Dummy test file that outputs data to indicate it ran."""

# Standard Library
import os
import pathlib


def test_set_output():
    """Write to output data."""
    output_path = pathlib.Path(os.environ["TEST_FILE"])
    output_path.unlink(missing_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as fp:
        fp.write("package_test_ran=1\n")
