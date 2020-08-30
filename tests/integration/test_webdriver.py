from assertpy import assert_that


def test_default_driver(default_driver):
    default_driver.get("https://www.google.com")
    assert_that(default_driver.current_url).is_equal_to("https://www.google.com/")
