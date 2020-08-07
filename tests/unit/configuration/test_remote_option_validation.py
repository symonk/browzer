import pytest
from assertpy import assert_that

from sylenium.configuration.sylenium_configuration import syleniumConfiguration
from sylenium.exceptions.exceptions import syleniumConfigValueError


class BrowserSubclass(syleniumConfiguration):
    def __init__(self, remote: bool):
        self.remote = remote


def test_browser_headless_on():
    assert_that(BrowserSubclass(remote=True).remote).is_true()


def test_browser_headless_off():
    assert_that(BrowserSubclass(remote=False).remote).is_false()


def test_browser_headless_type_checks():
    with pytest.raises(syleniumConfigValueError):
        BrowserSubclass(remote="exception")
