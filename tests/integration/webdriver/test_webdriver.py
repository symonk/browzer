from assertpy import assert_that

from sylenium.sylenium import go


def test_default_driver(default_driver) -> None:
    default_driver.get("https://www.google.com")
    assert_that(default_driver.get_current_url()).is_equal_to("https://www.google.com/")


def test_loading(webserver) -> None:
    go(webserver.page_url("simple_element"))
