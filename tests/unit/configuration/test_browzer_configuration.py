from assertpy import assert_that
from browzer.constants.strings import BROWZER_CONFIG

from browzer.configuration.BrowzerConfig import BrowzerConfiguration
from browzer.configuration.BrowzerConfig import load_browzer_config
from tests.test_files.custom_config import CustomConfig


def test_browzer_config_load():
    assert_that(load_browzer_config()).is_instance_of(BrowzerConfiguration)


def test_browzer_override(monkeypatch, test_files_config_classes):
    monkeypatch.setenv(BROWZER_CONFIG, test_files_config_classes)
    assert_that(load_browzer_config()).is_instance_of(CustomConfig)
