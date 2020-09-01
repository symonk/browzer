from assertpy import assert_that

from sylenium.configuration import Configuration


def test_sylenium_config_load(default_session):
    assert_that(default_session.config).is_instance_of(Configuration)
