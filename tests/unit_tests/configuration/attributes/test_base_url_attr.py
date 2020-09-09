import pytest
from assertpy import assert_that


def test_base_url_default(configuration):
    assert_that(configuration().base_url).is_none()


def test_base_url_override(configuration):
    link = "http://google.com"
    assert_that(configuration(base_url=link).base_url).is_equal_to(link)


def test_base_url_unsupported(configuration):
    with pytest.raises(TypeError) as error:
        configuration(base_url=12)
    assert_that(error.value.args[0]).is_equal_to(
        "base_url= should be of type: <class 'str'>"
    )


def test_base_url_none_is_ok(configuration):
    assert_that(configuration(base_url=None).base_url).is_none()


def test_base_url_invalid_url(configuration):
    link = "n0t a l1nk"
    with pytest.raises(ValueError) as error:
        configuration(base_url=link)
    assert_that(error.value.args[0]).is_equal_to(
        f"url: {link} is not considered a valid url"
    )
