import pytest
from assertpy import assert_that

from sylenium import Configuration


def test_browser_validation_is_enforced():
    with pytest.raises(ValueError):
        Configuration(browser="unsupported")


def test_browser_type_check_enforcement(default_session):
    with pytest.raises(ValueError):
        Configuration(browser="99")


def test_browser_chrome_is_ok():
    assert_that(Configuration(browser="chrome").browser).is_equal_to("chrome")
    assert_that(Configuration(browser="ChRoMe").browser).is_equal_to("chrome")


def test_firefox_is_ok():
    assert_that(Configuration(browser="firefox").browser).is_equal_to("firefox")
    assert_that(Configuration(browser="FiReFox").browser).is_equal_to("firefox")
