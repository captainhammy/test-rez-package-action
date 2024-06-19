"""Test the determine_package_name file."""

# Third Party
import pytest
import rez.exceptions

# test-rez-packages-action
import determine_package_name

# Tests


def test_get_package_name(shared_datadir):
    """Test determine_package_name.get_package_name()."""
    result = determine_package_name.get_package_name(shared_datadir)

    assert result == "test_package"

    # Test that an exception will be raised if the path does not contain a
    # package.py file.
    with pytest.raises(rez.exceptions.PackageMetadataError):
        determine_package_name.get_package_name(shared_datadir.parent)


def test_write_result(monkeypatch, tmp_path):
    """Test determine_package_name.write_result()."""
    output_file = tmp_path / "test_output.txt"

    monkeypatch.setenv("GITHUB_OUTPUT", output_file.as_posix())

    determine_package_name.write_result("test_package")

    with output_file.open() as handle:
        assert handle.read() == "package_name=test_package\n"
