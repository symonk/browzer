import pytest
from assertpy import assert_that

from sylenium.configuration.configuration import Configuration
from sylenium.exceptions.exceptions import syleniumConfigValueError


class BrowserSubclass(Configuration):
    def __init__(self, browser):
        self.browser = browser


def test_browser_validation_is_enforced():
    with pytest.raises(syleniumConfigValueError):
        BrowserSubclass(browser="unsupported")


def test_browser_chrome_is_ok():
    assert_that(BrowserSubclass(browser="chrome").browser).is_equal_to("chrome")


def test_firefox_is_ok():
    assert_that(BrowserSubclass(browser="firefox").browser).is_equal_to("firefox")
