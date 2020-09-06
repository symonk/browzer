import pytest
from assertpy import assert_that


def test_page_loading_strategy_supported(configuration):
    assert_that(
        configuration(page_loading_strategy="Fast").page_loading_strategy
    ).is_equal_to("fast")
    assert_that(configuration().page_loading_strategy).is_equal_to("fast")


def test_page_loading_strategy(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(page_loading_strategy=True)
    assert_that(exc.value.args[0]).is_equal_to(
        "page_loading_strategy= should be of type: <class 'str'>"
    )


def test_page_loading_strategy_unsupported(configuration):
    with pytest.raises(ValueError) as exc:
        configuration(page_loading_strategy="snail")
    assert_that(exc.value.args[0]).is_equal_to(
        "value: snail was not in the supported values: {'fast'}"
    )
