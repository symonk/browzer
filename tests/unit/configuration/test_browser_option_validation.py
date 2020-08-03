import pytest
from assertpy import assert_that

from browzer.configuration.browzer_configuration import BrowzerConfiguration
from browzer.exceptions.exceptions import BrowzerConfigValueError


class BrowserSubclass(BrowzerConfiguration):
    def __init__(self, browser):
        self.browser = browser


def test_browser_validation_is_enforced():
    with pytest.raises(BrowzerConfigValueError):
        BrowserSubclass(browser="unsupported")


def test_browser_chrome_is_ok():
    assert_that(BrowserSubclass(browser="chrome").browser).is_equal_to("chrome")


def test_firefox_is_ok():
    assert_that(BrowserSubclass(browser="firefox").browser).is_equal_to("firefox")
