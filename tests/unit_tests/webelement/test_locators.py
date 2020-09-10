from assertpy import assert_that
from selenium.webdriver.common.by import By

from sylenium.element import ByClassName
from sylenium.element import ByCssSelector
from sylenium.element import ById
from sylenium.element import ByLinkText
from sylenium.element import ByName
from sylenium.element import ByPartialLinkText
from sylenium.element import ByTagName
from sylenium.element import ByXpath


def test_by_id(random_string):
    assert_that(ById(random_string).locate()).is_equal_to((By.ID, random_string))


def test_by_xpath(random_string):
    assert_that(ByXpath(random_string).locate()).is_equal_to((By.XPATH, random_string))


def test_by_name(random_string):
    assert_that(ByName(random_string).locate()).is_equal_to((By.NAME, random_string))


def test_by_link_text(random_string):
    assert_that(ByLinkText(random_string).locate()).is_equal_to(
        (By.LINK_TEXT, random_string)
    )


def test_by_partial_link_text(random_string):
    assert_that(ByPartialLinkText(random_string).locate()).is_equal_to(
        (By.PARTIAL_LINK_TEXT, random_string)
    )


def test_by_tag_name(random_string):
    assert_that(ByTagName(random_string).locate()).is_equal_to(
        (By.TAG_NAME, random_string)
    )


def test_by_class_name(random_string):
    assert_that(ByClassName(random_string).locate()).is_equal_to(
        (By.CLASS_NAME, random_string)
    )


def test_by_css_selector(random_string):
    assert_that(ByCssSelector(random_string).locate()).is_equal_to(
        (By.CSS_SELECTOR, random_string)
    )
