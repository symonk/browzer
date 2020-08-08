import pytest

from sylenium.configuration.configuration import Configuration


def test_headless_on():
    cfg = Configuration()
    cfg.headless = True
    assert cfg.headless


def test_headless_off():
    cfg = Configuration()
    cfg.headless = False
    assert not cfg.headless


def test_browser_headless_type_checks():
    with pytest.raises(ValueError):
        Configuration().headless = "unsupported"
