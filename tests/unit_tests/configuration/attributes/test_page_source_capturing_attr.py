import pytest
from assertpy import assert_that


def test_page_source_capturing_on(configuration):
    assert_that(
        configuration(page_source_capturing=True).page_source_capturing
    ).is_true()


def test_page_source_capturing_off(configuration):
    assert_that(configuration(page_source_capturing=False).remote).is_false()


def test_page_source_capturing_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(page_source_capturing="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "page_source_capturing= should be of type: <class 'bool'>"
    )


def test_page_source_capturing_default(configuration):
    assert_that(configuration().page_source_capturing).is_false()
