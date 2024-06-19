"""Program to determine a local Rez package name."""

# Standard Library
import os
import pathlib

# Third Party
import rez.packages


def get_package_name(package_root: pathlib.Path) -> str:
    """Get the package name from the local package.py folder.

    Args:
        package_root: The package directory.

    Returns:
        The package name.
    """
    package = rez.packages.get_developer_package(package_root.as_posix())

    return package.name


def write_result(package_name: str) -> None:
    """Write the package name to the outputs file.

    Args:
        package_name: The local package name.
    """
    output_path = pathlib.Path(os.environ["GITHUB_OUTPUT"])

    with output_path.open("a", encoding="utf-8") as fp:
        fp.write(f"package_name={package_name}\n")


if __name__ == "__main__":
    name = get_package_name(pathlib.Path.cwd())

    write_result(name)
