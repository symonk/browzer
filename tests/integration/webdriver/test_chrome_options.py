from assertpy import assert_that

from sylenium import Configuration


def test_chrome_options_headless_standalone(headless_session):
    assert_that(headless_session.get_driver())


def test_service_options_log(sy_session):
    with sy_session(
        configuration=Configuration(
            chrome_service_log_path="C:\selenium\sylenium.log", headless=True
        )
    ) as session:
        session.get_driver()
