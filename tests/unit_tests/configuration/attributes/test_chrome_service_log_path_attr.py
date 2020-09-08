import pytest
from assertpy import assert_that


def test_chrome_service_log_default(configuration):
    assert_that(configuration().chrome_service_log_path).is_none()


def test_chrome_service_log_custom(configuration, tmpdir):
    assert_that(
        configuration(chrome_service_log_path=str(tmpdir)).chrome_service_log_path
    ).is_equal_to(str(tmpdir))


def test_chrome_service_unsupported_type(configuration):
    with pytest.raises(ValueError) as err:
        configuration(chrome_service_log_path=125)
    assert_that(err.value.args[0]).is_equal_to(
        "chrome_service_log_path= should be of type: <class 'str'>"
    )
