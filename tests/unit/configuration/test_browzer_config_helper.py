import pytest
from assertpy import assert_that

from browzer import driver_manager


def test_browzer_config_helper():
    one = driver_manager.get_driver()
    two = driver_manager.get_driver()
    assert_that(id(one)).is_equal_to(id(two))


@pytest.fixture(autouse=True)
def thread_cleaner():
    yield
    driver_manager.terminate_driver()
