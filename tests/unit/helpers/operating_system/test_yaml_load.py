from assertpy import assert_that

from browzer.helpers.operating_system.environ import get_dictionary_from_yaml


def test_yaml_load_without_yaml_ending_is_empty_dict():
    assert_that(get_dictionary_from_yaml("noyamlending")).is_equal_to({})
