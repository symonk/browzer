import pytest
from assertpy import assert_that


def test_browser_capabilities_default(configuration):
    assert_that(configuration().browser_capabilities).is_none()


def test_browser_capabilities_custom(configuration):
    dictionary = {"a": "one", "b": "two"}
    assert_that(
        configuration(browser_capabilities=dictionary).browser_capabilities
    ).is_equal_to(dictionary)


def test_browser_capabilities_incorrect_type(configuration):
    with pytest.raises(TypeError) as error:
        configuration(browser_capabilities=1337)
    assert_that(error.value.args[0]).is_equal_to(
        "browser_capabilities= should be of type: <class 'dict'>"
    )
