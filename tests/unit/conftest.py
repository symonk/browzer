import pytest


@pytest.fixture
def test_files_config_classes():
    return "tests.test_files.custom_config.CustomConfig"


@pytest.fixture
def test_travis_config():
    return "tests.travis.travis_configuration.TravisConfiguration"
