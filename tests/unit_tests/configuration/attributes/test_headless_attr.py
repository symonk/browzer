import pytest
from assertpy import assert_that


def test_headless_on(configuration):
    assert_that(configuration(headless=True).headless).is_true()


def test_headless_off(configuration):
    assert_that(configuration(headless=False).headless).is_false()


def test_headless_bad_type(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(headless="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "headless= should be of type: <class 'bool'>"
    )


def test_headless_default(configuration):
    assert_that(configuration().headless).is_true()
