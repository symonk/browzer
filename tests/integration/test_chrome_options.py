from assertpy import assert_that

from sylenium import Configuration


def test_chrome_options_headless_standalone(sy_session):
    with sy_session(configuration=Configuration(headless=True)) as session:
        assert_that(session.get_driver()).is_true()
