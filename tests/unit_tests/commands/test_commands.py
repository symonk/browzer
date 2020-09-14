import pytest
from assertpy import assert_that

from sylenium import command_invoker
from sylenium.exception import IllegalElementCommandException


def test_invalid_type():
    value = "nope"
    with pytest.raises(IllegalElementCommandException) as error:
        command_invoker.execute(value)
    assert_that(error.value.args[0]).is_equal_to(
        f"Attempting to perform an illegal command through the command invoker: {value}"
    )
