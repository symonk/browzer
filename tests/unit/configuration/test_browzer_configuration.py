from assertpy import assert_that
from tests.test_files.custom_config import CustomConfig

from browzer.configuration.configuration import BrowzerConfiguration
from browzer.configuration.configuration import load_browzer_config
from browzer.constants.strings import BROWZER_CONFIGURATION


def test_browzer_config_load():
    assert_that(load_browzer_config()).is_instance_of(BrowzerConfiguration)


def test_browzer_override(monkeypatch, test_files_config_classes):
    monkeypatch.setenv(BROWZER_CONFIGURATION, test_files_config_classes)
    assert_that(load_browzer_config()).is_instance_of(CustomConfig)
