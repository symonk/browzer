import pytest
from assertpy import assert_that


def test_javascript_sendkeys_on(configuration):
    assert_that(configuration(javascript_sendkeys=True).javascript_sendkeys).is_true()


def test_javascript_sendkeys_off(configuration):
    assert_that(configuration(javascript_sendkeys=False).javascript_sendkeys).is_false()


def test_javascript_sendkeys_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(javascript_sendkeys="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "javascript_sendkeys= should be of type: <class 'bool'>"
    )


def test_javascript_sendkeys_default(configuration):
    assert_that(configuration().javascript_clicks).is_false()
