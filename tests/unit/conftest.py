import pytest
from tests.test_files.test_configs import HeadlessConfig


@pytest.fixture
def headless_config():
    return HeadlessConfig()
