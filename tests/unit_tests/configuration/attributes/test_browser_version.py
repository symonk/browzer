import pytest
from assertpy import assert_that


def test_browser_version_default(configuration):
    assert_that(configuration().browser_version).is_equal_to("latest")


def test_browser_version_override(configuration):
    assert_that(configuration(browser_version="84").browser_version).is_equal_to("84")


def test_browser_version_unsupported_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(browser_version=True)
    assert_that(exc.value.args[0]).is_equal_to(
        "browser_version= should be of type: <class 'str'>"
    )
