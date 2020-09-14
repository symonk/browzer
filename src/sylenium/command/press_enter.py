from typing import Any

from selenium.webdriver.common.keys import Keys

from sylenium.command.command import Command


class PressEnter(Command):
    def execute(self, **kwargs) -> Any:
        kwargs.pop("element").wrapped_element.send_keys(Keys.ENTER)
