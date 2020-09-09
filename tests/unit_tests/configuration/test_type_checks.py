import pytest
from assertpy import assert_that


def test_bools_into_numbers_raises(configuration):
    with pytest.raises(TypeError) as error:
        configuration(explicit_waiting=False)
    assert_that(error.value.args[0]).is_equal_to(
        "explicit_waiting= should be of type: <class 'float'>"
    )
