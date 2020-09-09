import pytest
from assertpy import assert_that


def test_stack_trace_capturing_on(configuration):
    assert_that(
        configuration(stack_trace_capturing=True).stack_trace_capturing
    ).is_true()


def test_stack_trace_capturing_off(configuration):
    assert_that(
        configuration(stack_trace_capturing=False).stack_trace_capturing
    ).is_false()


def test_stack_trace_capturing_incorrect_type(configuration):
    with pytest.raises(TypeError) as exc:
        configuration(stack_trace_capturing="notabool")
    assert_that(exc.value.args[0]).is_equal_to(
        "stack_trace_capturing= should be of type: <class 'bool'>"
    )


def test_stack_trace_capturing_default(configuration):
    assert_that(configuration().stack_trace_capturing).is_false()
