import pytest

from sylenium.configuration.configuration import Configuration


def test_remote_on():
    cfg = Configuration()
    cfg.remote = False
    assert not cfg.remote


def test_remote_off():
    cfg = Configuration()
    cfg.remote = False
    assert not cfg.remote


def test_browser_headless_type_checks():
    with pytest.raises(ValueError):
        Configuration().remote = "unsupported"
