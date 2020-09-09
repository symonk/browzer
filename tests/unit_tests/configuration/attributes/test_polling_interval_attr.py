import pytest
from assertpy import assert_that


def test_polling_interval_default(configuration):
    assert_that(configuration().polling_interval).is_equal_to(01.50)


def test_polling_interval_custom(configuration):
    assert_that(configuration(polling_interval=125.00).polling_interval).is_equal_to(
        125.00
    )


def test_polling_interval_incorrect_type(configuration):
    with pytest.raises(TypeError) as error:
        configuration(polling_interval=True)
    assert_that(error.value.args[0]).is_equal_to(
        "polling_interval= should be of type: <class 'float'>"
    )


def test_polling_interval_int_is_converted(configuration):
    assert_that(configuration(polling_interval=1337).polling_interval).is_equal_to(1337)
    assert_that(configuration(polling_interval=1338).polling_interval).is_type_of(float)
