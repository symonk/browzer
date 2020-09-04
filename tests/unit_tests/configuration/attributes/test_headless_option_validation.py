import pytest
from assertpy import assert_that
from pyfields import FieldTypeError

from sylenium.configuration.configuration import Configuration


def test_headless_on(sy_session):
    with sy_session(Configuration(headless=True)) as session:
        assert_that(session.config.headless).is_true()


def test_headless_off(sy_session):
    with sy_session(Configuration(headless=False)) as session:
        assert_that(session.config.headless).is_false()


def test_browser_headless_type_checks(sy_session):
    with pytest.raises(FieldTypeError):
        with sy_session() as session:
            session.config.headless = "unsupported"
