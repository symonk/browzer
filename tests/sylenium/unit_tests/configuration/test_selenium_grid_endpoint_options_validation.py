from assertpy import assert_that

from sylenium.configuration.configuration import Configuration


def test_getting_url_functions_correctly():
    grid_url = Configuration(
        selenium_grid_port=9999, selenium_grid_url="https://100.0.0.0/wd/hub"
    ).full_hub_endpoint()
    assert_that(grid_url).is_equal_to("https://100.0.0.0/wd/hub:9999/wd/hub")
