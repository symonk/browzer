from assertpy import assert_that
from sylenium.configuration.sylenium_configuration import syleniumConfiguration


class BrowserSubclass(syleniumConfiguration):
    def __init__(self, selenium_grid_url: str, selenium_grid_port: int):
        self.selenium_grid_url = selenium_grid_url
        self.selenium_grid_port = selenium_grid_port
        self.remote = True


def test_getting_url_functions_correctly():
    grid_url = BrowserSubclass(
        selenium_grid_port=9999, selenium_grid_url="https://100.0.0.0/wd/hub"
    ).full_hub_endpoint
    assert_that(grid_url).is_equal_to("https://100.0.0.0/wd/hub:9999/wd/hub")
