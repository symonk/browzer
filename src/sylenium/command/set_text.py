from typing import Any

from sylenium.command.command import Command


class SetText(Command):
    def execute(self, **kwargs) -> Any:
        kwargs.pop("element").wrapped_element.send_keys(kwargs.pop("text"))
