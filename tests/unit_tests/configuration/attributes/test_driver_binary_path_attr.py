import pytest
from assertpy import assert_that


def test_driver_binary_path_default(configuration):
    assert_that(configuration().driver_binary_path).is_equal_to("acquire")


def test_driver_binary_path_custom(configuration):
    custom = "custom"
    assert_that(
        configuration(driver_binary_path=custom).driver_binary_path
    ).is_equal_to(custom)


def test_driver_binary_path_invalid_type(configuration):
    with pytest.raises(TypeError) as err:
        configuration(driver_binary_path=True)
    assert_that(err.value.args[0]).is_equal_to(
        "driver_binary_path= should be of type: <class 'str'>"
    )
