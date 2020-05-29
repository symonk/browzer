import pytest


@pytest.fixture
def test_files_config_classes():
    yield "tests.test_files.custom_config.CustomConfig"
