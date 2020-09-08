import pytest
from assertpy import assert_that


def test_selenium_grid_port_default(configuration):
    assert_that(configuration().selenium_grid_port).is_equal_to(4444)


def test_selenium_grid_port_custom(configuration):
    assert_that(configuration(selenium_grid_port=9999).selenium_grid_port).is_equal_to(
        9999
    )


def test_selenium_grid_port_bad_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(selenium_grid_port=19.99)
    assert_that(exc.value.args[0]).is_equal_to(
        "selenium_grid_port= should be of type: <class 'int'>"
    )
