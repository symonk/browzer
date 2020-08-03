from assertpy import assert_that

from browzer.configuration.browzer_configuration import BrowzerConfiguration


class BrowserSubclass(BrowzerConfiguration):
    def __init__(self, headless: bool):
        self.headless = headless


def test_browser_headless_on():
    assert_that(BrowserSubclass(headless=True).headless).is_true()


def test_browser_headless_off():
    assert_that(BrowserSubclass(headless=False).headless).is_false()
