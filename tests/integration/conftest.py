import pytest

from browzer import driver_manager


@pytest.fixture(autouse=True)
def clean_up():
    yield
    driver_manager.terminate_driver()
