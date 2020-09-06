import pytest
from assertpy import assert_that


def test_remote_on(configuration):
    assert_that(configuration(remote=True).remote).is_true()


def test_remote_off(configuration):
    assert_that(configuration(remote=False).remote).is_false()


def test_remote_incorrect_type(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(remote="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "remote= should be of type: <class 'bool'>"
    )
