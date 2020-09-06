import pytest
from assertpy import assert_that


def test_proxy_enabled_on(configuration):
    assert_that(configuration(proxy_enabled=True).proxy_enabled).is_true()


def test_proxy_enabled_default_off(configuration):
    assert_that(configuration().proxy_enabled).is_false()


def test_proxy_enabled_unsupported_type(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(proxy_enabled="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "proxy_enabled= should be of type: <class 'bool'>"
    )
