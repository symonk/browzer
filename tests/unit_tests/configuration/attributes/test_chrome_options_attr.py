import pytest
from assertpy import assert_that
from selenium.webdriver.chrome.webdriver import Options as ChromeOptions


def test_chrome_options_default(configuration):
    assert_that(configuration().chrome_options).is_none()


def test_chrome_options_with_custom_options(configuration):
    optionz = {"abc", "def"}
    chrome_opts = ChromeOptions()
    for x in optionz:
        chrome_opts.add_argument(x)
    assert_that(configuration(chrome_options=chrome_opts).chrome_options).is_equal_to(
        chrome_opts
    )


def test_chrome_options_custom_set(configuration):
    options = {"abc" "123"}
    optionz = configuration(chrome_options=options).chrome_options
    assert_that(optionz.arguments[0]).is_equal_to("".join(options))


def test_chrome_options_incorrect_type(configuration):
    with pytest.raises(TypeError) as err:
        configuration(chrome_options=99)
    assert_that(err.value.args[0]).is_equal_to(
        "chrome_options= should be of type: <class 'set'> <class 'selenium.webdriver.chrome.options.Options'>"
    )
