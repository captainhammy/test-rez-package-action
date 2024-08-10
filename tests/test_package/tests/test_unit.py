"""Dummy test file that outputs data to indicate it ran."""

# Standard Library
import os
import pathlib


def test_set_output():
    """Write to output data.

    This doesn't really do much since we don't export the outputs from the action
    itself.
    """
    output_path = pathlib.Path(os.environ["TEST_TEMP_DIR"]) / "unit.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("a", encoding="utf-8") as fp:
        fp.write("package_test_ran=1\n")
