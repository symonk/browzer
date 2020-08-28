from assertpy import assert_that

from sylenium.configuration import Configuration
from sylenium.configuration import config


def test_sylenium_config_load():
    assert_that(config).is_instance_of(Configuration)
