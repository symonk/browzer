from assertpy import assert_that

from sylenium.configuration.configuration import Configuration


def test_getting_url_functions_correctly():
    expected = "https://100.0.0.0:9999/wd/hub"
    assert_that(
        Configuration(
            selenium_grid_port=9999, selenium_grid_url="https://100.0.0.0"
        ).full_hub_endpoint()
    ).is_equal_to(expected)
