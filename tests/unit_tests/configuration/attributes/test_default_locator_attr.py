import pytest
from assertpy import assert_that


def test_default_selector_default(configuration):
    assert_that(configuration().default_selector).is_equal_to("css")


def test_default_selector_custom(configuration):
    assert_that(configuration(default_selector="xpath").default_selector).is_equal_to(
        "xpath"
    )


def test_default_selector_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(default_selector=20)
    assert_that(exc.value.args[0]).is_equal_to(
        "default_selector= should be of type: <class 'str'>"
    )
