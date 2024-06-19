"""Dummy test file that outputs data to indicate it ran."""

# Standard Library
import os
import pathlib


def test_set_output():
    """Write to output data."""
    output_path = pathlib.Path(os.environ["GITHUB_OUTPUT"])
    print(output_path.as_posix())

    with output_path.open("a", encoding="utf-8") as fp:
        fp.write("package_test_ran=1\n")

    print(f"Wrote output to {output_path.as_posix()}")

    with output_path.open("r", encoding="utf-8") as fp:
        print(fp.read())
