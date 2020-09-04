import pytest
from assertpy import assert_that
from pyfields import FieldTypeError

from sylenium.configuration.configuration import Configuration


def test_remote_on(sy_session):
    with sy_session(configuration=Configuration(remote=True)) as session:
        assert_that(session.config.remote).is_true()


def test_remote_off(sy_session):
    with sy_session(configuration=Configuration(remote=False)) as session:
        assert_that(session.config.remote).is_false()


def test_browser_headless_type_checks(sy_session):
    with pytest.raises(FieldTypeError):
        with sy_session() as session:
            session.config.remote = "unsupported"
