import pytest
from assertpy import assert_that


def test_maximized_default(configuration):
    assert_that(configuration().maximized).is_true()


def test_maximized_override(configuration):
    assert_that(configuration(maximized=False).maximized).is_false()


def test_maximized_unsupported(configuration):
    with pytest.raises(ValueError) as error:
        configuration(maximized="")
    assert_that(error.value.args[0]).is_equal_to(
        "maximized= should be of type: <class 'bool'>"
    )
