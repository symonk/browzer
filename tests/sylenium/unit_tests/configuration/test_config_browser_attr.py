import pytest
from assertpy import assert_that

from sylenium import Session
from sylenium.configuration.configuration import Configuration


def test_browser_validation_is_enforced(default_session):
    with pytest.raises(ValueError):
        default_session.config.browser = "unsupported"


def test_browser_type_check_enforcement(default_session):
    with pytest.raises(ValueError):
        default_session.config.browser = 99.00


def test_browser_chrome_is_ok():
    with Session(Configuration(browser="chrome")) as session:
        assert_that(session.config.browser).is_equal_to("chrome")


def test_firefox_is_ok():
    with Session(Configuration(browser="firefox")) as session:
        assert_that(session.config.browser).is_equal_to("firefox")
