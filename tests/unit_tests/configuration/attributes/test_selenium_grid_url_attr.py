import pytest
from assertpy import assert_that


def test_selenium_grid_url_bad_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(selenium_grid_url=True)
    assert_that(exc.value.args[0]).is_equal_to(
        "selenium_grid_url= should be of type: <class 'str'>"
    )


def test_selenium_grid_url_default(configuration):
    assert_that(configuration().selenium_grid_url).is_equal_to("http://localhost")


def test_selenium_grid_url_custom(configuration):
    url = "https://www.google.com"
    assert_that(configuration(selenium_grid_url=url).selenium_grid_url).is_equal_to(url)
