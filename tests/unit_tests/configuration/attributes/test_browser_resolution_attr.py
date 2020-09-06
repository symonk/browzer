import pytest
from assertpy import assert_that


def test_browser_resolution_default(configuration):
    assert_that(configuration().browser_resolution).is_none()


def test_browser_resolution_with_none_is_ok(configuration):
    assert_that(configuration(browser_resolution=None).browser_resolution).is_none()


def test_browser_resolution_incorrect_type(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(browser_resolution=True)
    assert_that(exc.value.args[0]).is_equal_to(
        "browser_resolution= should be of type: <class 'str'>"
    )


def test_browser_resolution_contains_x(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(browser_resolution="1920")
    assert_that(exc.value.args[0]).is_equal_to(
        "browser_resolution= should contain 'x' to decipher width vs height"
    )
