from assertpy import assert_that

from sylenium.configuration.configuration import Configuration


def test_getting_url_functions_correctly(sy_session):
    with sy_session(
        Configuration(selenium_grid_port=9999, selenium_grid_url="https://100.0.0.0")
    ) as session:
        assert_that(session.config.full_hub_endpoint()).is_equal_to(
            "https://100.0.0.0:9999/wd/hub"
        )
