from assertpy import assert_that

from sylenium.helpers._os_environ_helper import read_from_environ


def test_environ_successfully(monkeypatch):
    key, val = "monkey", "dummy"
    monkeypatch.setenv(key, val)
    assert_that(read_from_environ(key, None)).is_equal_to(val)


def test_environ_unsuccessfully():
    default = "default"
    assert_that(read_from_environ("foobar", default)).is_equal_to(default)
