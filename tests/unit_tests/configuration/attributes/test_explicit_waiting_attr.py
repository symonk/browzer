import pytest
from assertpy import assert_that


def test_explicit_waiting_default(configuration):
    assert_that(configuration().explicit_waiting).is_equal_to(30.00)


def test_explicit_waiting_custom(configuration):
    assert_that(configuration(explicit_waiting=125.00).explicit_waiting).is_equal_to(
        125.00
    )


def test_explicit_waiting_incorrect_type(configuration):
    with pytest.raises(TypeError) as error:
        configuration(explicit_waiting="nope")
    assert_that(error.value.args[0]).is_equal_to(
        "explicit_waiting= should be of type: <class 'float'>"
    )


def test_explicit_waiting_int_is_converted(configuration):
    assert_that(configuration(explicit_waiting=1337).explicit_waiting).is_equal_to(1337)
    assert_that(configuration(explicit_waiting=1338).explicit_waiting).is_type_of(float)
