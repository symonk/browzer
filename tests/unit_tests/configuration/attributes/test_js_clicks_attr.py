import pytest
from assertpy import assert_that


def test_javascript_clicks_on(configuration):
    assert_that(configuration(javascript_clicks=True).javascript_clicks).is_true()


def test_javascript_clicks_off(configuration):
    assert_that(configuration(javascript_clicks=False).javascript_clicks).is_false()


def test_javascript_clicks_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(javascript_clicks="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "javascript_clicks= should be of type: <class 'bool'>"
    )


def test_javascript_clicks_default(configuration):
    assert_that(configuration().javascript_clicks).is_false()
