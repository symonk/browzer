import pytest
from assertpy import assert_that

from sylenium.constants import SUPPORTED_BROWSERS


def test_browser_unsupported_value(configuration):
    test_browser = "unsupported"
    with pytest.raises(ValueError) as exc:
        configuration(browser=test_browser)
    assert_that(exc.value.args[0]).is_equal_to(
        f"value: {test_browser} was not in the supported values: {SUPPORTED_BROWSERS}"
    )


def test_browser_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(browser=99)
    assert_that(exc.value.args[0]).is_equal_to(
        "browser= should be of type: <class 'str'>"
    )


def test_browser_lowers_successful(configuration):
    assert_that(configuration(browser="chrome").browser).is_equal_to("chrome")
    assert_that(configuration(browser="ChroME").browser).is_equal_to("chrome")
    assert_that(configuration(browser="firefox").browser).is_equal_to("firefox")
    assert_that(configuration(browser="FiReFox").browser).is_equal_to("firefox")


def test_browser_default(configuration):
    assert_that(configuration().browser).is_equal_to("chrome")
