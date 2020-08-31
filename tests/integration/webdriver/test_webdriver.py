from assertpy import assert_that

from sylenium.sylenium import load


def test_default_driver(default_driver):
    default_driver.get("https://www.google.com")
    assert_that(default_driver.current_url).is_equal_to("https://www.google.com/")


def test_loading(default_session, webserver):
    load(webserver.page_url("simple_element"))
