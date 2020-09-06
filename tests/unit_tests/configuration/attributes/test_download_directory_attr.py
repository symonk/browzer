import pytest
from assertpy import assert_that


def test_download_dir_default(configuration):
    assert_that(configuration().download_directory).is_none()


def test_download_dir_with_none(configuration):
    assert_that(configuration(download_directory=None).download_directory).is_none()


def test_download_dir_unsupported_type(configuration):
    with pytest.raises(FileExistsError) as exc:
        configuration(download_directory="notadir")
    assert_that(exc.value.args[0]).is_equal_to(
        "Directory: notadir was not found on the file system"
    )


def test_download_dir_valid_directory(configuration, tmpdir):
    assert_that(
        configuration(download_directory=str(tmpdir)).download_directory
    ).is_equal_to(str(tmpdir))
